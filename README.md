# Secure Pritam's Chatbot 🔐💬

This is a **secure chatbot application** built using **Streamlit** and **Firebase Authentication**. It integrates with **Microsoft Copilot** to provide AI-powered responses while ensuring user authentication.

---

## 🚀 Features

- **User Authentication** (Login & Signup using Firebase)
- **Secure Authentication Handling**
- **Microsoft Copilot Integration**
- **Streamlit UI with Custom Styling**
- **Session Management**

---

## 📂 Folder Structure
```
Authenticate_Chat_Bot_Pritam/
│-- chatbot-a42f1-firebase-adminsdk.json  # Firebase Credentials (Replace with your own)
│-- app.py                                  # Main Streamlit App
│-- .env                                    # Environment Variables (Optional)
│-- requirements.txt                        # Python Dependencies
│-- README.md                               # Documentation
```

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
```sh
$ git clone https://github.com/your-username/Authenticate_Chat_Bot_Pritam.git
$ cd Authenticate_Chat_Bot_Pritam
```

### 2️⃣ Create & Activate a Virtual Environment
```sh
$ python -m venv venv
$ source venv/bin/activate  # On macOS/Linux
$ venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 4️⃣ Setup Firebase Authentication
- Create a **Firebase Project** in [Firebase Console](https://console.firebase.google.com/).
- Enable **Email/Password Authentication** in Firebase Authentication settings.
- Download the **Firebase Admin SDK JSON file** and place it in the project folder.
- Ensure the correct path is set in `app.py`:
  ```python
  cred = credentials.Certificate("chatbot.json")
  ```

### 5️⃣ Run the Application
```sh
$ streamlit run app.py
```

---

## 🛠 Troubleshooting

**Common Issues & Fixes:**

1️⃣ **Invalid JWT Signature Error**
   - Ensure the correct **Firebase Admin SDK JSON** is being used.
   - Check that Firebase authentication is **enabled** in the console.

2️⃣ **User Already Exists Error**
   - The email is **already registered**. Try logging in instead.
   - Use Firebase Console to delete existing users if needed.

3️⃣ **ModuleNotFoundError: No module named 'firebase_admin'**
   - Run `pip install firebase-admin` to install the missing package.

---

## ✨ Contributing
Feel free to fork the project and submit **pull requests** with improvements!

---

## 📜 License
This project is licensed under the **MIT License**.

---

**Made with ❤️ by Pritam** 🚀
