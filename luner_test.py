import gymnasium as gym

env = gym.make("LunarLander-v2", render_mode="human")
observation, info = env.reset(seed=42)

render_interval = 100
iteration = 0

while True:
    action = env.action_space.sample()  # this is where you would insert your policy
    observation, reward, terminated, truncated, info = env.step(action)
    iteration += 10000  

    if iteration % render_interval == 0:
        env.render()

    if terminated or truncated:
        observation, info = env.reset()
        iteration = 0

env.close()

