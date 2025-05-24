
# 🌟 VisageMorpherAura

> **Real-Time Interactive Face Replacement Powered by Large Language Models**

VisageMorpherAura is a cutting-edge real-time AI application that allows users to **interact with a selection of generated celebrity faces** and seamlessly **replace their own face in a live camera feed** using intuitive **hand gestures and voice commands**.

This project combines advanced **face generation**, **gesture recognition**, and **face swapping** in one immersive experience — powered by **LLMs**, a **Go backend**, and a **TypeScript frontend**.

---

## ✨ Key Features

- 🎤 **Voice-Activated Generation**: Call out names like *"Elon Musk"*, *"Taylor Swift"*, or other famous figures to generate 3–5 sample images of their faces using LLM-assisted image generation models.
  
- 🖐️ **Hand-Based Selection**: Point at your favorite face using your hand through a webcam. The system detects and interprets your gesture to select it.

- 📷 **Live Face Replacement**: Your selected face is mapped and blended onto your own in real-time using advanced face morphing techniques.

- ⚡ **Real-Time Interaction**: All steps are performed with low-latency for an engaging and responsive experience.

- 🤖 **LLM-Driven Prompting**: Use Large Language Models to generate or guide image prompts (e.g., emotion, lighting, style).

---

## 🛠️ Tech Stack

| Layer | Tools & Frameworks |
|-------|---------------------|
| **Frontend** | TypeScript, React, WebRTC/WebSocket, TensorFlow.js (hand tracking) |
| **Backend** | Go (Golang), Gin/Fiber/FiberGo for API server |
| **AI/ML** | PyTorch or TensorFlow (for face gen & swap), LLM APIs (e.g., OpenAI, HuggingFace Transformers) |
| **Model Inference** | Image Generation (e.g., Stable Diffusion, LLM-guided), Face Swapping (e.g., SimSwap, DeepFaceLab) |
| **Gesture Control** | MediaPipe or OpenCV for hand tracking |
| **Voice Command** | Web Speech API (frontend) or Vosk (backend) |

---

## 🧠 System Architecture

```txt
[Voice Input]         [Webcam Feed]
     ↓                     ↓
[Frontend (React + TS)] ← Gesture Detection
     ↓                        ↓
[WebSocket + HTTP] ⇄ [Go Backend API]
     ↓                        ↓
[LLM Prompting] ←→ [Face Generation Engine]
     ↓
[Face Selection UI] → [Live Face Replacement]
```

## 🚀 How It Works

1. **User speaks a name** (e.g., "Generate Elon Musk").
2. **LLM or fine-tuned model generates facial image prompts**.
3. Backend generates **3–5 face images** using diffusion models.
4. User **points at a face** using their hand → gesture detected.
5. Face is selected and swapped in **real-time onto user’s face** in webcam view.
6. Optionally supports multiple personas and recording.

---

## 🧩 Use Cases

- 🎥 **Streaming Filters**: Realtime facial overlays for streamers.
- 👨‍🏫 **Education / Fun Demos**: AI-powered face impersonation.
- 🧪 **AI Research Showcase**: Multi-modal interaction using LLM, vision, and audio inputs.

---

📂 Project Structure (suggested)
 
```
visage-morpher-aura/
├── backend/                  # Golang backend API
│   └── main.go
├── frontend/                 # React + TypeScript frontend
│   ├── components/
│   └── App.tsx
├── model/                    # Inference server, model configs
│   └── facegen.py
├── scripts/                  # Dev tools and helpers
├── README.md
└── LICENSE

```

📦 Future Enhancements
- [ ] Emotion-aware generation (happy Elon Musk vs. angry Elon Musk)
- [ ] ARKit support for 3D head pose estimation
- [ ] Mobile support (React Native)
- [ ] Multi-face selection with swipe interface
- [ ] Privacy-preserving local-only mode

## 📝 License

This project is licensed under the [Apache License 2.0](./LICENSE).

---

## 🙌 Contributing

Pull requests and feedback are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 🧑‍💻 Author

**Trần Phi Hùng** – [LinkedIn](https://linkedin.com) · [GitHub](https://github.com)


---

> _“VisageMorpherAura — Real-Time AI Face Transformation with the Essence of Identity.” – VisageMorpherAura_