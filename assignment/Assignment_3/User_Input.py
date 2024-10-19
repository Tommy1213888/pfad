import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Noise generation function
def generate_noise(shape, scale, mean, distribution):
    if distribution == "正态分布 (Normal)":
        noise = np.random.normal(loc=mean, scale=scale, size=shape)
    elif distribution == "均匀分布 (Uniform)":
        noise = np.random.uniform(low=mean - scale, high=mean + scale, size=shape)
    else:
        noise = np.random.normal(loc=mean, scale=scale, size=shape)
    return noise

# Texture generation function
def generate_texture(shape, scale, sigma, mean, distribution):
    noise = generate_noise(shape, scale, mean, distribution)
    texture = gaussian_filter(noise, sigma=sigma)
    texture = np.clip(texture, 0, 1)
    return texture

# Title
st.title("自定义噪波纹理生成器 (Custom Noise Texture Generator)")

# User input
st.sidebar.header("参数设置 (Parameter Settings)")

# Texture type selection
texture_type = st.sidebar.selectbox(
    "选择生成的纹理类型 (Select Texture Type):",
    ["火山 (Volcano)", "草地 (Grassland)", "雪面 (Snow)", "自定义 (Custom)"]
)

# Parameters dictionary
params = {
    "shape_size": 512,
    "scale": 20,
    "sigma": 3,
    "mean": 0.5,
    "distribution": "正态分布 (Normal)",
    "colormap": "gray"
}

# Parameter adjustments based on texture type
if texture_type == "火山 (Volcano)":
    st.sidebar.subheader("火山参数调整 (Volcano Parameters)")
    params["shape_size"] = st.sidebar.slider("纹理尺寸 (Texture Size):", 256, 1024, 512, step=64)
    params["scale"] = st.sidebar.slider("噪声尺度 (Noise Scale):", 10.0, 50.0, 30.0)
    params["sigma"] = st.sidebar.slider("高斯模糊程度 (Gaussian Blur Sigma):", 1.0, 10.0, 5.0)
    params["mean"] = st.sidebar.slider("平均值 (Mean):", 0.0, 1.0, 0.5)
    params["distribution"] = st.sidebar.selectbox("噪声分布类型 (Noise Distribution):", ["正态分布 (Normal)", "均匀分布 (Uniform)"])
    params["colormap"] = st.sidebar.selectbox("颜色映射 (Colormap):", ["inferno", "hot", "autumn"])
elif texture_type == "草地 (Grassland)":
    st.sidebar.subheader("草地参数调整 (Grassland Parameters)")
    params["shape_size"] = st.sidebar.slider("纹理尺寸 (Texture Size):", 256, 1024, 512, step=64)
    params["scale"] = st.sidebar.slider("噪声尺度 (Noise Scale):", 5.0, 30.0, 20.0)
    params["sigma"] = st.sidebar.slider("高斯模糊程度 (Gaussian Blur Sigma):", 1.0, 10.0, 3.0)
    params["mean"] = st.sidebar.slider("平均值 (Mean):", 0.0, 1.0, 0.4)
    params["distribution"] = st.sidebar.selectbox("噪声分布类型 (Noise Distribution):", ["正态分布 (Normal)", "均匀分布 (Uniform)"])
    params["colormap"] = st.sidebar.selectbox("颜色映射 (Colormap):", ["Greens", "YlGn", "summer"])
elif texture_type == "雪面 (Snow)":
    st.sidebar.subheader("雪面参数调整 (Snow Parameters)")
    params["shape_size"] = st.sidebar.slider("纹理尺寸 (Texture Size):", 256, 1024, 512, step=64)
    params["scale"] = st.sidebar.slider("噪声尺度 (Noise Scale):", 1.0, 20.0, 15.0)
    params["sigma"] = st.sidebar.slider("高斯模糊程度 (Gaussian Blur Sigma):", 0.1, 5.0, 1.0)
    params["mean"] = st.sidebar.slider("平均值 (Mean):", 0.5, 1.0, 0.8)
    params["distribution"] = st.sidebar.selectbox("噪声分布类型 (Noise Distribution):", ["正态分布 (Normal)", "均匀分布 (Uniform)"])
    params["colormap"] = st.sidebar.selectbox("颜色映射 (Colormap):", ["Blues", "cool", "winter"])
else:
    st.sidebar.subheader("自定义参数调整 (Custom Parameters)")
    params["shape_size"] = st.sidebar.slider("纹理尺寸 (Texture Size):", 256, 1024, 512, step=64)
    params["scale"] = st.sidebar.slider("噪声尺度 (Noise Scale):", 1.0, 50.0, 20.0)
    params["sigma"] = st.sidebar.slider("高斯模糊程度 (Gaussian Blur Sigma):", 0.1, 10.0, 3.0)
    params["mean"] = st.sidebar.slider("平均值 (Mean):", 0.0, 1.0, 0.5)
    params["distribution"] = st.sidebar.selectbox("噪声分布类型 (Noise Distribution):", ["正态分布 (Normal)", "均匀分布 (Uniform)"])
    params["colormap"] = st.sidebar.selectbox("颜色映射 (Colormap):", plt.colormaps())

# Generate texture
if st.button("生成纹理 (Generate Texture)"):
    shape = (params["shape_size"], params["shape_size"])
    texture = generate_texture(shape, params["scale"], params["sigma"], params["mean"], params["distribution"])

    # Display texture
    plt.figure(figsize=(6, 6))
    plt.imshow(texture, cmap=params["colormap"])
    plt.axis('off')
    st.pyplot(plt)
