from crew import MBACrew
from dotenv import load_dotenv

load_dotenv()  # Load .env variables


def main():
    crew = MBACrew()
    print("\n🎓 MBA Advisor CLI (type 'exit' to quit)\n")

    while True:
        user_input = input("🧑 You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 Goodbye!")
            break

        response = crew.run(user_input)
        print(f"\n🤖 Advisor:\n{response}\n")


if __name__ == "__main__":
    main()
