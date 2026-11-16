
import tkinter as tk

# WINDOWS LOCK SIMULATOR
DURATION = 24 * 60 * 60
remaining = DURATION

root = tk.Tk()
root.title("SYSTEM LOCK SIMULATOR")
root.configure(bg="#080808")
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)

# Safe emergency exit using ESC
root.bind("<Escape>", lambda e: root.destroy())

title = tk.Label(
    root,
    text="⚠ SYSTEM LOCK SIMULATOR",
    fg="#ff3030",
    bg="#080808",
    font=("Consolas", 30, "bold")
)
title.pack(pady=55)

subtitle = tk.Label(
    root,
    text="WINDOWS SECURITY SIMULATION",
    fg="#aaaaaa",
    bg="#080808",
    font=("Consolas", 15)
)
subtitle.pack(pady=10)

warning = tk.Label(
    root,
    text="SIMULATED SYSTEM RESTRICTION",
    fg="#ff3030",
    bg="#080808",
    font=("Consolas", 23, "bold")
)
warning.pack(pady=35)

timer = tk.Label(
    root,
    text="24:00:00",
    fg="#ffffff",
    bg="#080808",
    font=("Consolas", 65, "bold")
)
timer.pack(pady=25)

info = tk.Label(
    root,
    text="Simulation active - No Windows files modified",
    fg="#00cc88",
    bg="#080808",
    font=("Consolas", 14)
)
info.pack(pady=20)

def update_timer():
    global remaining

    if remaining <= 0:
        timer.config(text="00:00:00")
        warning.config(
            text="SIMULATION COMPLETED",
            fg="#00cc88"
        )
        info.config(text="Windows simulation ended.")
        return

    hours = remaining // 3600
    minutes = (remaining % 3600) // 60
    seconds = remaining % 60

    timer.config(
        text=f"{hours:02}:{minutes:02}:{seconds:02}"
    )

    remaining -= 1
    root.after(1000, update_timer)

footer = tk.Label(
    root,
    text="EDUCATIONAL PROJECT | SAFE SIMULATION",
    fg="#555555",
    bg="#080808",
    font=("Consolas", 10)
)
footer.pack(side="bottom", pady=25)

update_timer()
root.mainloop()
