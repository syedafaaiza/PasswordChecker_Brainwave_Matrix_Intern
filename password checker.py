#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install pillow


# In[10]:


import tkinter as tk
import re

def password_strength_checker(password):
    length_criteria = len(password) >= 8
    complexity_criteria = (
        re.search(r"[a-z]", password) and
        re.search(r"[A-Z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    )
    uniqueness_criteria = len(set(password)) >= 6

    strength_score = 0
    if length_criteria:
        strength_score += 1
    if complexity_criteria:
        strength_score += 1
    if uniqueness_criteria:
        strength_score += 1

    if strength_score == 3:
        feedback = "Your password is strong!"
        color = "green"
    elif strength_score == 2:
        feedback = "Your password is moderate. Consider adding more complexity."
        color = "orange"
    elif strength_score == 1:
        feedback = "Your password is weak. Please improve its strength."
        color = "red"
    else:
        feedback = "Your password is very weak. It must be at least 8 characters long and contain a mix of letters, numbers, and special characters."
        color = "red"

    return feedback, color

def check_password_strength():
    password = password_entry.get()
    feedback, color = password_strength_checker(password)
    result_label.config(text=feedback, fg=color)
    password_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")

password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

root.mainloop()


# In[ ]:





# In[ ]:




