import random
from telegram import Update
from telegram.ext import ContextTypes
from tips import TIPS

MOTIVATIONS = [
    "Every expert was once a beginner. Keep going! 💪",
    "Your consistency today is building your freedom tomorrow. 🔥",
    "Allah does not burden a soul beyond what it can bear. Trust the process. 🙏",
    "The pain you feel today is the strength you feel tomorrow. 💡",
    "You are not behind. You are on your own timeline. ⏳",
    "Small daily progress beats perfect someday. 🚀",
    "The best time to start was yesterday. The next best time is now. ⚡",
    "Difficulty is what makes achievement meaningful. Stay strong. 🌟",
    "You have survived every hard day so far. Today is no different. 🙌",
    "Your story is still being written. Don't close the book yet. 📖",
]

QUIZ_QUESTIONS = [
    {
        "question": "What is the smallest deployable unit in Kubernetes?",
        "options": ["A) Container", "B) Pod", "C) Node", "D) Cluster"],
        "answer": "B",
        "explanation": "A Pod is the smallest deployable unit in Kubernetes. It can contain one or more containers that share storage and network."
    },
    {
        "question": "Which command shows running Docker containers?",
        "options": ["A) docker list", "B) docker show", "C) docker ps", "D) docker run"],
        "answer": "C",
        "explanation": "docker ps shows all currently running containers. Add -a to see stopped containers too."
    },
    {
        "question": "What does CI/CD stand for?",
        "options": ["A) Code Integration/Code Deployment", "B) Continuous Integration/Continuous Deployment", "C) Container Integration/Container Deployment", "D) Cloud Integration/Cloud Deployment"],
        "answer": "B",
        "explanation": "CI/CD stands for Continuous Integration and Continuous Deployment — automating testing and deployment of code."
    },
    {
        "question": "What file does Docker use to build an image?",
        "options": ["A) docker.yml", "B) docker.json", "C) Dockerfile", "D) docker.config"],
        "answer": "C",
        "explanation": "A Dockerfile contains instructions that Docker uses to build an image automatically."
    },
    {
        "question": "Which Git command saves changes to the repository?",
        "options": ["A) git save", "B) git push", "C) git add", "D) git commit"],
        "answer": "D",
        "explanation": "git commit saves your staged changes to the local repository with a message describing what changed."
    },
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to DevOps Learning Bot!\n\n"
        "I am your personal DevOps tutor built by 0xApana 🚀\n\n"
        "Here is what I can do:\n"
        "/tip - Get a random DevOps tip\n"
        "/roadmap - See the DevOps learning roadmap\n"
        "/explain - Learn about a DevOps tool\n"
        "/quiz - Test your DevOps knowledge\n"
        "/resources - Get learning resources\n"
        "/about - Learn about the creator\n\n"
        "Let's build something great together! 💪"
    )

async def tip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    categories = {
        "linux": [t for t in TIPS if t.startswith("Linux")],
        "docker": [t for t in TIPS if t.startswith("Docker")],
        "git": [t for t in TIPS if t.startswith("Git")],
        "k8s": [t for t in TIPS if t.startswith("K8s")],
        "cicd": [t for t in TIPS if t.startswith("CI/CD")],
        "devops": [t for t in TIPS if t.startswith("DevOps")],
    }

    if args:
        category = args[0].lower()
        tips_list = categories.get(category, [])
        if tips_list:
            await update.message.reply_text(f"💡 {random.choice(tips_list)}")
        else:
            await update.message.reply_text(
                "Available categories:\n"
                "/tip linux\n"
                "/tip docker\n"
                "/tip git\n"
                "/tip k8s\n"
                "/tip cicd\n"
                "/tip devops"
            )
    else:
        random_tip = random.choice(TIPS)
        await update.message.reply_text(f"💡 {random_tip}")

async def roadmap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🗺 DevOps Learning Roadmap:\n\n"
        "1️⃣ Linux Fundamentals\n"
        "2️⃣ Git & GitHub\n"
        "3️⃣ Docker & Containers\n"
        "4️⃣ CI/CD Pipelines\n"
        "5️⃣ Kubernetes\n"
        "6️⃣ Cloud - AWS/Azure\n\n"
        "Stay consistent. Trust the process. 💪"
    )

async def explain(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text(
            "Please specify a tool.\n"
            "Example: /explain docker"
        )
        return

    tool = args[0].lower()
    explanations = {
        "docker": "🐳 Docker packages your application and its entire environment together so it runs the same everywhere. Think of it as oxygen giving life to an image.",
        "kubernetes": "☸️ Kubernetes manages, scales and automates deployment of containers across multiple machines. Think of it as a city manager controlling many buildings.",
        "git": "📝 Git tracks changes in your code and allows collaboration. Think of it as a time machine for your code.",
        "linux": "🐧 Linux is an open source operating system that powers most of the world's servers and cloud infrastructure.",
        "cicd": "⚙️ CI/CD automates testing and deployment of your code. Think of it as a factory assembly line for software.",
        "aws": "☁️ AWS is Amazon's cloud platform offering computing, storage, and hundreds of services on demand.",
    }

    response = explanations.get(tool, f"Sorry I don't have an explanation for '{tool}' yet. More coming soon!")
    await update.message.reply_text(response)

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = random.choice(QUIZ_QUESTIONS)
    context.user_data["quiz_answer"] = question["answer"]
    context.user_data["quiz_explanation"] = question["explanation"]

    options = "\n".join(question["options"])
    await update.message.reply_text(
        f"🧠 DevOps Quiz Time!\n\n"
        f"Question: {question['question']}\n\n"
        f"{options}\n\n"
        f"Reply with A, B, C, or D! 🤔"
    )

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if "quiz_answer" not in context.user_data:
        return

    answer = update.message.text.strip().upper()
    correct = context.user_data.get("quiz_answer")
    explanation = context.user_data.get("quiz_explanation")
    motivation = random.choice(MOTIVATIONS)

    if answer not in ["A", "B", "C", "D"]:
        return

    if answer == correct:
        await update.message.reply_text(
            f"✅ CORRECT! Well done!\n\n"
            f"📖 {explanation}\n\n"
            f"💬 {motivation}\n\n"
            f"Type /quiz for another question! 🔥"
        )
    else:
        await update.message.reply_text(
            f"❌ Wrong answer! The correct answer is {correct}.\n\n"
            f"📖 {explanation}\n\n"
            f"💬 {motivation}\n\n"
            f"Type /quiz to try again! 💪"
        )

    context.user_data.pop("quiz_answer", None)
    context.user_data.pop("quiz_explanation", None)

async def resources(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 DevOps Learning Resources:\n\n"
        "🎥 YouTube Channels:\n"
        "• TechWorld with Nana - Best DevOps channel\n"
        "• FreeCodeCamp - Full courses free\n"
        "• KodeKloud - Hands on labs\n"
        "• Kunal Kushwaha - Beginner friendly\n\n"
        "🌐 Websites:\n"
        "• roadmap.sh/devops - Visual roadmap\n"
        "• docs.docker.com - Docker official docs\n"
        "• kubernetes.io/docs - K8s official docs\n"
        "• linuxcommand.org - Linux basics\n\n"
        "💡 Tip: Consistency beats intensity. 30 mins daily beats 5 hours once a week!"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👨‍💻 About the Creator:\n\n"
        "Name: Ridwanullahi Ali Apana\n"
        "Handle: 0xApana\n"
        "Role: Aspiring Cloud & DevOps Engineer\n\n"
        "🛠 Skills:\n"
        "Linux • Git • Docker • CI/CD • Kubernetes • AWS\n\n"
        "🔗 Links:\n"
        "GitHub: github.com/0xApana\n"
        "Fiverr: fiverr.com/apana0x\n\n"
        "💬 This bot was built as part of my DevOps learning journey.\n"
        "Building real skills, one container at a time. 🚀"
    )
