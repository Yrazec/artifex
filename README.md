# 🎨 Artifex

Welcome to **Artifex** - your personal AI artist! ✨

Artifex is a powerful command-line tool for locally generating stunning images using **Stable Diffusion XL**. Create breathtaking artwork right on your machine with full control over every parameter. It supports GPU/CPU inference, flexible YAML configuration, custom prompts, and automatically timestamps generated images for seamless batch workflows.

> 🌟 **Artifex** - Latin for "artist" / "creator"

### ✨ What is Artifex?

Artifex empowers you to harness the power of cutting-edge AI image generation technology **on your own hardware**. No cloud dependencies, no API costs-just pure creative freedom running locally on your machine. Whether you're an artist exploring new visual styles, a designer prototyping ideas, or an experimenter curious about generative AI, Artifex gives you the tools to bring your imagination to life.

### 🖼️ Example Output

![Viking](outputs/images/20260710_130934.png "Viking")

```
Prompt: 
A legendary Viking warrior standing on a windswept Nordic
coastline at sunset, massive muscular build, long braided
hair and beard, wearing detailed fur cloak, weathered leather
armor, engraved iron helmet, holding a battle axe, ancient
Norse runes carved into metal and wood, dramatic mountains
and fjords in the background, stormy sky with golden light
rays, epic cinematic atmosphere, ultra realistic, highly
detailed textures, realistic skin, intricate armor details,
fantasy realism, heroic pose, volumetric lighting, depth of
field, 8k quality, masterpiece, cinematic photography 

Negative Prompt: 
low quality, blurry, pixelated, bad anatomy, deformed body,
extra fingers, missing fingers, poorly drawn hands, distorted
face, asymmetrical eyes, unrealistic proportions, duplicate
person, extra limbs, bad armor design, plastic skin, cartoon,
anime, CGI look, oversaturated colors, flat lighting, low
detail, watermark, text, logo, signature, cropped, out of
frame, jpeg artifacts 

device: cuda
seed: 42

model:
    type: sdxl
    checkpoint: stabilityai/stable-diffusion-xl-base-1.0

generation:
    width: 1024
    height: 1024
    steps: 20
    guidance_scale: 4.0
```

### 🎯 Key Features

- **🖥️ Local Processing** - Run everything locally on your GPU or CPU. No internet required after initial model download
- **⚙️ Full Control** - YAML-based configuration for fine-tuning every aspect of image generation (steps, guidance, dimensions, etc.)
- **📝 Flexible Prompts** - Support for positive and negative prompts to guide the AI exactly how you want
- **⏱️ Auto-Timestamped** - Every generated image is automatically timestamped for easy organization and batch workflows
- **🚀 GPU Acceleration** - Blazing-fast inference with CUDA support, with fallback to CPU
- **🎭 Professional Quality** - Leverages Stable Diffusion XL for state-of-the-art image synthesis
- **🔄 Batch Processing** - Perfect for automated creative workflows and batch image generation

## 📋 Prerequisites & Requirements

Before diving in, make sure you have everything ready! ✅

### 🐍 Python Version

**Required:** Python 3.11.x

> 💡 **Tip:** Make sure you're using the correct Python version. Check with `python --version`

> ⚡ **Note:** GPU acceleration requires NVIDIA hardware and CUDA drivers. CPU-only mode works on any machine but generates images slower.

## 🚀 Installation Guide

Follow these steps carefully to set up Artifex on your system. Don't worry-it's easier than it sounds! 🎉

### Step 1: 🔧 Setup Virtual Environment

A virtual environment keeps your project dependencies isolated and clean. Create one now:

```commandline
python -m venv .venv
```

Activate the virtual environment:

```commandline
.venv\Scripts\activate
```

You should see `(.venv)` in your terminal prompt. Perfect! ✨

Upgrade pip to get the latest tools:

```commandline
python -m pip install --upgrade pip
```

### Step 2: 🚀 Install PyTorch with CUDA Support

This is the deep learning framework that powers everything. Install PyTorch with CUDA 12.1 support for GPU acceleration:

```commandline
python -m pip install torch==2.5.1+cu121 torchvision==0.20.1+cu121 torchaudio==2.5.1+cu121 --index-url https://download.pytorch.org/whl/cu121
```

**Prefer CPU-only mode?** Use this alternative:
```commandline
python -m pip install torch torchvision torchaudio
```

> 📦 This is a large download (~3GB). Grab some coffee! ☕

### Step 3: 🎯 Install the Diffusion Stack

These are the core packages that enable AI image generation. Install them one by one:

**Diffusers** - The generative AI library that implements Stable Diffusion:
```commandline
pip install diffusers==0.26.3
```

**Transformers** - Hugging Face transformers for language understanding:
```commandline
pip install transformers==4.38.2
```

**Hugging Face Hub** - Download and manage pre-trained models:
```commandline
pip install huggingface_hub==0.20.3
```

**Accelerate** - Distributed training and inference optimization:
```commandline
pip install accelerate==0.27.2
```

**SafeTensors** - Safe, efficient model serialization format:
```commandline
pip install safetensors
```

**Pillow** - Image processing and manipulation:
```commandline
pip install pillow
```

> 💾 Combined, these packages are about 2-3GB. Your internet connection will thank you when it's done! 🎉

### Step 4: ✅ Verify Everything Works

Run this verification script to ensure all dependencies are installed correctly with the right versions. The project includes `verify.py` for this exact purpose:

```python
import accelerate
import diffusers
import huggingface_hub
import torch
import torchvision
import transformers


assert accelerate.__version__ == "0.27.2"
assert diffusers.__version__ == "0.26.3"
assert huggingface_hub.__version__ == "0.20.3"
assert torch.__version__ == "2.5.1+cu121"
assert torchvision.__version__ == "0.20.1+cu121"
assert transformers.__version__ == "4.38.2"

assert torch.cuda.is_available() == True

print("All versions match!")
```

**Run it with:**
```commandline
python verify.py
```

✅ If you see "All versions match!", you're good to go! 🎉

> 💡 **Troubleshooting:** If any assertions fail, double-check the version numbers you installed match the requirements above. Version mismatches can cause subtle bugs!

## 🎬 Usage Guide & Complete Workflow

Ready to create some beautiful images? Let's dive in! 🚀

### 🖼️ Basic Image Generation

The simplest way to generate an image with Artifex:

```commandline
python -m artifex.cli --config configs/local.yaml --prompt-file prompts/example.txt
```

**What happens:**
1. Reads your generation config from `configs/local.yaml`
2. Loads your creative prompt from `prompts/example.txt`
3. Initializes the Stable Diffusion XL model
4. Generates a beautiful image
5. Saves it with a timestamp to `outputs/`

### 🚫 Advanced: With Negative Prompts

Sometimes it's helpful to tell the AI what you *don't* want. Use negative prompts to guide the generation away from unwanted elements:

```commandline
python -m artifex.cli --config configs/local.yaml --prompt-file prompts/example.txt --negative-prompt-file prompts/example_negative.txt
```

**Example negative prompt:** "blurry, low quality, distorted, ugly" - this tells the AI to avoid these characteristics.

### 📝 Inline Prompts (No Files!)

You can also pass prompts directly without files:

```commandline
python -m artifex.cli --config configs/local.yaml --prompt "a majestic dragon flying over mountains, oil painting style"
```

### 📁 Understanding Configuration Files

#### **`configs/local.yaml`** - Your Generation Blueprint

This YAML file controls every aspect of image generation:

```yaml
device: cuda              # Use 'cuda' for GPU or 'cpu' for CPU
seed: 42                  # Random seed for reproducibility (same seed = same image)

model:
    type: sdxl            # Always 'sdxl' for Stable Diffusion XL
    checkpoint: stabilityai/stable-diffusion-xl-base-1.0  # Model identifier

generation:
    width: 1024           # Image width in pixels (e.g., 512, 768, 1024)
    height: 1024          # Image height in pixels (must match width for square images)
    steps: 20             # Number of diffusion steps (20-50: higher = more detailed but slower)
    guidance_scale: 4.0   # How closely to follow the prompt (1-20: higher = more prompt-focused)
```

**💡 Tips for tweaking parameters:**
- `steps`: 20-30 for fast drafts, 40-50 for high quality
- `guidance_scale`: 3-7 for balanced results, 7-15 for prompt-heavy generation
- `seed`: Same seed produces identical images-useful for reproducibility and iteration
- `width/height`: 768x768 or 1024x1024 are sweet spots for quality vs speed

#### **`prompts/example.txt`** - Your Creative Vision

This is where your imagination lives! Write detailed, descriptive prompts:

```
a cyberpunk city at night, neon lights reflecting on wet streets, 
flying cars, holographic advertisements, rain, cinematic lighting, 
4K, digital art, trending on artstation
```

**🎨 Pro Tips for Better Prompts:**
- Be **specific and descriptive** - More detail = better results
- **Include art style** - "oil painting", "digital art", "concept art", "anime", etc.
- **Add quality descriptors** - "high quality", "masterpiece", "4K", "detailed"
- **Specify mood/lighting** - "cinematic", "dramatic lighting", "golden hour", etc.
- **Reference artists/styles** - "trending on artstation", "by Studio Ghibli", etc.

#### **`prompts/example_negative.txt`** - What to Avoid

Tell the AI what you don't want to see:

```
blurry, low quality, distorted, ugly, deformed, amateur, 
watermark, text, signature, poorly drawn
```

### ⚙️ Complete Generation Flow (Step-by-Step)

Here's everything that happens when you run Artifex:

1. **🔍 Parse Arguments** → Reads your CLI parameters (config, prompts, etc.)
2. **📂 Load Configuration** → Reads YAML config file and validates settings
3. **📝 Load Prompts** → Reads positive (and optional negative) prompts from files
4. **🎛️ Initialize Pipeline** → Creates the SDXL pipeline with your device (GPU/CPU)
5. **⬇️ Download Models** → Automatically downloads and caches SDXL (~13.2 GB) on first run
6. **🔧 Configure Generation** → Sets up all generation parameters (steps, guidance, dimensions)
7. **🤖 Run Inference** → Processes your prompts through the AI model
8. **🖼️ Generate Image** → Creates the final image through iterative diffusion
9. **💾 Save Output** → Timestamps and saves to `outputs/` directory
10. **✅ Complete** → Done! Check your masterpiece! 🎉

### 📤 Output Organization

All generated images are automatically saved to `outputs/` with timestamps:

```
outputs/
├── image_20240710_143052.png
├── image_20240710_143847.png
├── image_20240710_144512.png
└── ...
```

This makes it easy to track when each image was created and organize batches!

## 🤖 AI Models & Model Caching

### Understanding SDXL (Stable Diffusion XL)

**Stable Diffusion XL (SDXL)** is a state-of-the-art text-to-image generative AI model developed by Stability AI. It's an upgrade from the original Stable Diffusion with:

- 🎨 **Better Image Quality** - More detailed and coherent images
- 📝 **Superior Prompt Understanding** - Better at following detailed instructions
- 🚀 **Faster Generation** - More efficient inference
- 🎯 **Improved Composition** - Better spatial reasoning and layout

### 📥 Automatic Model Downloading

On your **first run**, Artifex will automatically download the SDXL model from Hugging Face Hub. This happens transparently-just wait for it to complete!

**Download happens at:** `artifex/pipeline/sdxl.py`
```python
self.pipe = diffusers.StableDiffusionXLPipeline.from_pretrained(checkpoint, torch_dtype=dtype)
```

> ⏱️ **First run?** Expect 5-20 minutes depending on your internet speed. Subsequent runs are instant!

### 💾 Model Cache Location

Model checkpoints are automatically downloaded from **Hugging Face Hub** and cached locally for future use:

**Windows Cache Directory:**
```text
%USERPROFILE%\.cache\huggingface
```

**Example full path:**
```
C:\Users\YourUsername\.cache\huggingface\hub\models--stabilityai--stable-diffusion-xl-base-1.0\snapshots\...
```

### 📦 Model Size & Storage

**SDXL Model:** ~13.2 GB total
- 39 files
- 16 directories
- Contains weights, configs, tokenizers, and more

> 💡 **Pro Tip:** After the first download, the models are cached. Subsequent runs use the cached version-lightning fast! ⚡

### 🔄 Multiple Models Support

Want to use different models? Edit `configs/local.yaml`:

```yaml
model:
    checkpoint: stabilityai/stable-diffusion-xl-base-1.0  # Official SDXL base
```

Other compatible checkpoints from Hugging Face:
- `stabilityai/stable-diffusion-xl-refiner-1.0` - Refiner variant
- Community fine-tuned SDXL models
- Custom models you've trained

> 📝 Each model you use gets cached separately-disk space can add up!

## 🏗️ Project Architecture

Curious how everything works under the hood? Here's the structure:

```
artifex/
├── cli.py                      # 🖥️ Command-line interface entrypoint
├── pipeline/
│   └── sdxl.py                 # 🤖 Stable Diffusion XL pipeline wrapper
├── io/
│   └── input_output.py         # 📂 File I/O operations (load configs, prompts)
└── utils/
    ├── constants.py            # ⚙️ Global constants and settings
    ├── logger.py               # 📝 Logging utilities
    └── handle_warnings.py      # ⚠️ Warning suppression
```

### 🔄 Module Overview

- **`cli.py`** - Entry point that handles command-line arguments and orchestrates the workflow
- **`pipeline/sdxl.py`** - Wrapper around the Diffusers library that manages SDXL model initialization and image generation
- **`io/input_output.py`** - Handles loading YAML configs and text prompts, saving generated images
- **`utils/`** - Helper modules for logging, constants, and warning management

### 📊 Data Flow Diagram

```
User Input (CLI args)
    ↓
Parse Arguments & Config
    ↓
Load Prompts (positive & negative)
    ↓
Initialize SDXL Pipeline
    ↓
Download Models (if needed)
    ↓
Generate Image
    ↓
Save with Timestamp
    ↓
Output: Beautiful Image! 🎨
```

## 🎓 Tips, Tricks & Best Practices

### ⚡ Performance Optimization

**Make Artifex faster:**
- **Use GPU** - GPU generation is 10-50x faster than CPU. Always prefer GPU when available!
- **Lower Steps for Drafts** - Use 20-25 steps for quick previews, 40-50 for final quality
- **Batch Workflows** - Generate multiple images in a script loop for efficient batch processing
- **Seed Management** - Use fixed seeds when iterating on prompts for reproducible results
- **Memory Management** - Close other applications to free up VRAM for smoother generation

### 🎨 Advanced Prompting Techniques

**Structure your prompt like this:**
```
[Subject] [Action/Pose] [Style] [Lighting] [Atmosphere] [Quality] [Platform]
```

**A real example:**
```
A majestic cat wearing steampunk goggles, sitting on a floating cloud island, 
digital art style, golden hour lighting, surreal, volumetric lighting, 
highly detailed, masterpiece, 4K, trending on artstation and deviantart
```

**What makes prompts better:**
- ✅ Specific and highly descriptive (not generic)
- ✅ Includes artistic medium/style ("digital art", "oil painting", "3D render")
- ✅ Mentions lighting and mood ("cinematic", "dramatic", "warm", "cool")
- ✅ Quality modifiers ("high quality", "masterpiece", "4K", "ultra-detailed")
- ✅ Reference artists or styles ("trending on artstation", "by Greg Rutkowski")
- ❌ Too vague or one-word descriptions
- ❌ Contradictory instructions
- ❌ Overly long (keep it under 150 words ideally)

### 🔍 Debugging & Troubleshooting

**Getting weird or artifacts in results?**
- Check your negative prompt-it might be too aggressive
- Try reducing `guidance_scale` (7.5-10 is often sweet spot)
- Increase `steps` for more refinement
- Use a fixed `seed` to reproduce and debug issues systematically
- Experiment with different prompts to isolate the problem

**Model not downloading or loading?**
- Verify all package versions match in `verify.py`
- Check your internet connection (need speed for 13GB download)
- Ensure you have at least 20GB free disk space
- Try deleting cached model and re-downloading: `rm -r ~/.cache/huggingface/`
- Restart Python interpreter if changes don't apply

**Getting out of memory (OOM) errors?**
- Reduce image dimensions (try 768x768 instead of 1024x1024)
- Lower number of steps (20 instead of 40)
- Use CPU mode if GPU VRAM is insufficient (slower but works)
- Close other GPU-consuming applications

**Slow generation even with GPU?**
- Check CUDA is actually available: `python -c "import torch; print(torch.cuda.is_available())"`
- Verify you're using the right PyTorch version with CUDA support
- Check GPU isn't being throttled by temperature or power limits

### 📚 Learning Resources

**Want to dive deeper?**
- 🔗 [Hugging Face Diffusers Documentation](https://huggingface.co/docs/diffusers/)
- 🔗 [Stable Diffusion XL Paper](https://arxiv.org/abs/2307.01952)
- 🔗 [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)
- 🔗 [Stability AI Official Docs](https://platform.stability.ai/docs/)

## 🚀 Quick Start Checklist

Follow this checklist to get up and running in minutes:

- [ ] ✅ **Python 3.11.x** installed (`python --version`)
- [ ] ✅ **Virtual environment** created (`.venv\Scripts\activate`)
- [ ] ✅ **PyTorch + CUDA** installed (test with `import torch; print(torch.cuda.is_available())`)
- [ ] ✅ **Diffusion stack** installed (all 6 packages)
- [ ] ✅ **`verify.py`** runs successfully with "All versions match!"
- [ ] ✅ **Sample configs** in place (`configs/local.yaml`)
- [ ] ✅ **Ready to create!** 🎉

### 🎬 Your First Generation

```commandline
python -m artifex.cli --config configs/local.yaml --prompt-file prompts/example.txt
```

**Expected output:**
- See INFO log messages as pipeline initializes
- Model downloads on first run (~13GB, takes 5-20 minutes)
- Watch as your image is generated step-by-step
- Check `outputs/` folder for your newly created masterpiece! 🖼️

---

## 💬 Questions or Issues?

- 🐛 Found a bug? Check the code in `artifex/`
- 🤔 Have a question? Review the detailed sections above
- 📖 Want to learn more? Check out the Learning Resources section
- 💡 Have a suggestion? Feel free to explore the codebase

#  
###### Cezary Pietruszyński ∙ [LinkedIn](https://www.linkedin.com/in/cezary-pietruszynski-tkd/)
_Yrazec is just Cezary but reversed!_
