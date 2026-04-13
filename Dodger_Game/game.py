import streamlit as st
import random
import time

st.set_page_config(page_title="Dodger Game", layout="centered")

# Initialize session state
if "player_x" not in st.session_state:
    st.session_state.player_x = 5  # position (0-10 grid)
    st.session_state.enemies = []
    st.session_state.score = 0
    st.session_state.game_over = False

GRID_WIDTH = 10
GRID_HEIGHT = 10

st.title("🎮 Dodger Game (Streamlit Version)")

# Controls
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬅️ Left") and not st.session_state.game_over:
        if st.session_state.player_x > 0:
            st.session_state.player_x -= 1

with col3:
    if st.button("➡️ Right") and not st.session_state.game_over:
        if st.session_state.player_x < GRID_WIDTH - 1:
            st.session_state.player_x += 1

# Spawn enemies
if not st.session_state.game_over:
    if random.random() < 0.3:
        st.session_state.enemies.append([random.randint(0, GRID_WIDTH - 1), 0])

# Move enemies
new_enemies = []
for enemy in st.session_state.enemies:
    enemy[1] += 1
    if enemy[1] < GRID_HEIGHT:
        new_enemies.append(enemy)
    else:
        st.session_state.score += 1

st.session_state.enemies = new_enemies

# Collision check
for enemy in st.session_state.enemies:
    if enemy[1] == GRID_HEIGHT - 1 and enemy[0] == st.session_state.player_x:
        st.session_state.game_over = True

# Draw grid
grid = [["⬛" for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Draw enemies
for enemy in st.session_state.enemies:
    grid[enemy[1]][enemy[0]] = "🟥"

# Draw player
grid[GRID_HEIGHT - 1][st.session_state.player_x] = "🟦"

# Display grid
for row in grid:
    st.write(" ".join(row))

# Score
st.subheader(f"Score: {st.session_state.score}")

# Game Over
if st.session_state.game_over:
    st.error("💀 GAME OVER!")
    if st.button("🔄 Restart"):
        st.session_state.player_x = 5
        st.session_state.enemies = []
        st.session_state.score = 0
        st.session_state.game_over = False

# Auto refresh (game loop simulation)
if not st.session_state.game_over:
    time.sleep(0.5)
    st.rerun()