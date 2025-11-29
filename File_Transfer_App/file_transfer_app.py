"""
File Transfer App - A simple file transfer simulation system
"""

import os
import shutil
from datetime import datetime


class FileTransferApp:
    """File Transfer application for managing file operations."""

    def __init__(self, base_directory=None):
        """Initialize the file transfer app."""
        if base_directory is None:
            base_directory = os.getcwd()
        self.base_directory = base_directory
        self.transfer_history = []

    def list_files(self, directory=None):
        """List all files in a directory."""
        if directory is None:
            directory = self.base_directory

        try:
            items = os.listdir(directory)
            files = []
            folders = []

            for item in items:
                full_path = os.path.join(directory, item)
                if os.path.isfile(full_path):
                    size = os.path.getsize(full_path)
                    files.append((item, size))
                else:
                    folders.append(item)

            return True, {"files": files, "folders": folders}
        except (FileNotFoundError, PermissionError) as e:
            return False, str(e)

    def get_file_info(self, filepath):
        """Get information about a file."""
        try:
            if not os.path.exists(filepath):
                return False, "File not found."

            stat = os.stat(filepath)
            info = {
                "name": os.path.basename(filepath),
                "path": os.path.abspath(filepath),
                "size": stat.st_size,
                "created": datetime.fromtimestamp(
                    stat.st_ctime
                ).strftime("%Y-%m-%d %H:%M:%S"),
                "modified": datetime.fromtimestamp(
                    stat.st_mtime
                ).strftime("%Y-%m-%d %H:%M:%S"),
                "is_file": os.path.isfile(filepath),
                "is_dir": os.path.isdir(filepath)
            }
            return True, info
        except (FileNotFoundError, PermissionError) as e:
            return False, str(e)

    def copy_file(self, source, destination):
        """Copy a file from source to destination."""
        try:
            if not os.path.exists(source):
                return False, "Source file not found."

            if os.path.isdir(source):
                return False, "Source is a directory. Use copy_directory."

            shutil.copy2(source, destination)
            self._log_transfer("COPY", source, destination)
            return True, f"File copied to {destination}"
        except (FileNotFoundError, PermissionError, shutil.SameFileError) as e:
            return False, str(e)

    def move_file(self, source, destination):
        """Move a file from source to destination."""
        try:
            if not os.path.exists(source):
                return False, "Source file not found."

            shutil.move(source, destination)
            self._log_transfer("MOVE", source, destination)
            return True, f"File moved to {destination}"
        except (FileNotFoundError, PermissionError, shutil.SameFileError) as e:
            return False, str(e)

    def delete_file(self, filepath):
        """Delete a file."""
        try:
            if not os.path.exists(filepath):
                return False, "File not found."

            if os.path.isdir(filepath):
                os.rmdir(filepath)
            else:
                os.remove(filepath)
            self._log_transfer("DELETE", filepath, "N/A")
            return True, "File deleted successfully."
        except (FileNotFoundError, PermissionError, OSError) as e:
            return False, str(e)

    def create_directory(self, directory_path):
        """Create a new directory."""
        try:
            os.makedirs(directory_path, exist_ok=True)
            self._log_transfer("CREATE_DIR", "N/A", directory_path)
            return True, f"Directory created: {directory_path}"
        except (FileNotFoundError, PermissionError, OSError) as e:
            return False, str(e)

    def rename_file(self, old_path, new_name):
        """Rename a file or directory."""
        try:
            if not os.path.exists(old_path):
                return False, "File not found."

            directory = os.path.dirname(old_path)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            self._log_transfer("RENAME", old_path, new_path)
            return True, f"Renamed to: {new_name}"
        except (FileNotFoundError, PermissionError, OSError) as e:
            return False, str(e)

    def _log_transfer(self, operation, source, destination):
        """Log file transfer operation."""
        self.transfer_history.append({
            "operation": operation,
            "source": source,
            "destination": destination,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def get_transfer_history(self):
        """Get transfer history."""
        if not self.transfer_history:
            return "No transfer history."
        result = []
        for record in self.transfer_history:
            result.append(
                f"[{record['timestamp']}] {record['operation']}: "
                f"{record['source']} -> {record['destination']}"
            )
        return "\n".join(result)

    @staticmethod
    def format_size(size_bytes):
        """Format file size to human readable format."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} PB"


def main():
    """Main function to run the file transfer app."""
    app = FileTransferApp()

    print("=" * 50)
    print("       Welcome to File Transfer App")
    print("=" * 50)
    print(f"Current Directory: {app.base_directory}")

    while True:
        print("\n" + "-" * 50)
        print("1. List Files")
        print("2. Get File Info")
        print("3. Copy File")
        print("4. Move File")
        print("5. Delete File")
        print("6. Create Directory")
        print("7. Rename File/Directory")
        print("8. View Transfer History")
        print("9. Change Directory")
        print("10. Exit")
        print("-" * 50)

        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            success, result = app.list_files()
            if success:
                print("\n📁 Folders:")
                for folder in result["folders"]:
                    print(f"  📂 {folder}")
                print("\n📄 Files:")
                for name, size in result["files"]:
                    print(f"  📄 {name} ({app.format_size(size)})")
            else:
                print(result)

        elif choice == "2":
            filepath = input("Enter file path: ")
            success, info = app.get_file_info(filepath)
            if success:
                print(f"\nName: {info['name']}")
                print(f"Path: {info['path']}")
                print(f"Size: {app.format_size(info['size'])}")
                print(f"Created: {info['created']}")
                print(f"Modified: {info['modified']}")
                print(f"Type: {'File' if info['is_file'] else 'Directory'}")
            else:
                print(info)

        elif choice == "3":
            source = input("Enter source file path: ")
            destination = input("Enter destination path: ")
            success, msg = app.copy_file(source, destination)
            print(msg)

        elif choice == "4":
            source = input("Enter source file path: ")
            destination = input("Enter destination path: ")
            success, msg = app.move_file(source, destination)
            print(msg)

        elif choice == "5":
            filepath = input("Enter file path to delete: ")
            confirm = input("Are you sure? (y/n): ")
            if confirm.lower() == "y":
                success, msg = app.delete_file(filepath)
                print(msg)
            else:
                print("Deletion cancelled.")

        elif choice == "6":
            dir_path = input("Enter directory path to create: ")
            success, msg = app.create_directory(dir_path)
            print(msg)

        elif choice == "7":
            old_path = input("Enter file/directory path: ")
            new_name = input("Enter new name: ")
            success, msg = app.rename_file(old_path, new_name)
            print(msg)

        elif choice == "8":
            print("\n📋 Transfer History:")
            print(app.get_transfer_history())

        elif choice == "9":
            new_dir = input("Enter new directory path: ")
            if os.path.isdir(new_dir):
                app.base_directory = os.path.abspath(new_dir)
                print(f"Changed to: {app.base_directory}")
            else:
                print("Invalid directory.")

        elif choice == "10":
            print("\nThank you for using File Transfer App. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
