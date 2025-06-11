#!/home/devx100/bashai/.venv/bin/python3 
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM , AutoModelForCausalLM
import subprocess # Import the subprocess module

# loading tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("archan01/byt5-small-finetuned")
model = AutoModelForSeq2SeqLM.from_pretrained("archan01/byt5-small-finetuned")

print("Enter your natural language command (type 'quit' to exit):")

while True:
    nl = input("> ").strip() # Use a prompt for better UX
    if nl.lower() == "quit": # Use .lower() for case-insensitive quit
        break

    model_input = f"Write bash command for : {nl}"

    model_input = tokenizer(
        model_input,
        max_length=128,
        padding="max_length",
        truncation=True,
        return_tensors='pt'
    )

    generated_ids = model.generate(**model_input)
    response = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    print(f"\nGenerated Command: {response}")

    confirmation = input("Press 'e' to execute, or any other character to cancel: ").lower() # .lower() for case-insensitive input

    if confirmation == 'e':
        print("\nExecuting command...")
        try:
            # Use subprocess.run() for executing the command
            # shell=True is used here because the model generates a full shell command string
            # capture_output=False (default) means output goes directly to your console
            # check=True will raise an exception if the command returns a non-zero exit code
            subprocess.run(response, shell=True, check=True)
            print("\nCommand executed successfully.")
        except subprocess.CalledProcessError as e:
            # This block catches errors if the executed command itself fails
            print(f"\nError executing command: Command exited with code {e.returncode}")
            # print(f"Stdout: {e.stdout.decode().strip()}") # Uncomment if you want to see captured stdout on error
            # print(f"Stderr: {e.stderr.decode().strip()}") # Uncomment if you want to see captured stderr on error
        except FileNotFoundError:
            print("\nError: The command or one of its components was not found. Check your PATH.")
        except Exception as e:
            print(f"\nAn unexpected error occurred during execution: {e}")
    else:
        print("Command execution cancelled.")
    print("-" * 50) # Separator for clarity