class OnboardingWizard:
    def __init__(self):
        self.steps = [
            {"title": "Step 1: Registration", "description": "Please register to continue"},
            {"title": "Step 2: Profile Setup", "description": "Please set up your profile"},
            {"title": "Step 3: Account Verification", "description": "Please verify your account"},
            {"title": "Step 4: Final Setup", "description": "Please complete the final setup"}
        ]
        self.current_step = 0

    def display_step(self):
        step = self.steps[self.current_step]
        print(f"Step {self.current_step + 1}: {step['title']}")
        print(step['description'])

    def next_step(self):
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
        else:
            print("Onboarding complete!")

    def previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1

    def run(self):
        while True:
            self.display_step()
            action = input("What would you like to do? (next/previous/exit): ")
            if action.lower() == "next":
                self.next_step()
            elif action.lower() == "previous":
                self.previous_step()
            elif action.lower() == "exit":
                break
            else:
                print("Invalid action. Please try again.")

wizard = OnboardingWizard()
wizard.run()
