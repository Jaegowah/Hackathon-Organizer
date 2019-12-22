from tkinter import *


def launch_hackathon_dashboard(my_hackathon):
    window = Tk()
    window.title("Hackathon Dashboard v0.1")
    window.geometry("1600x1000")

    header_frame = Frame(window, bg="green")
    timer_label = Label(header_frame, text="00min 00sec")
    phase_label = Label(header_frame, text="Current Phase: Work")

    footer_frame = Frame(window)
    title_label = Label(footer_frame, text=my_hackathon.hackathon_id)
    exit_button = Button(footer_frame, text="Quit Tool", command=window.quit)

    main_frame = Frame(window, bg="blue")
    player_labels = []

    for player in my_hackathon.players.values():
         player_labels.append(Label(main_frame, text=player.player_name))


# header
    header_frame.place(relwidth=0.98, relheight=0.1, relx=0.5, rely=0.055, anchor="center")
    timer_label.place(relheight=0.2, relx=0.5, rely=0.25, anchor="center")
    phase_label.place(relheight=0.2, relx=0.5, rely=0.75, anchor="center")

# main block
    main_frame.place(relwidth=0.98, relheight=0.5, relx=0.5, rely=0.5, anchor="center")
    for i, label in enumerate(player_labels):
        label.place(relx=i/10, rely=0.5, anchor="center")

# footer
    title_label.place(relwidth=0.2, relheight=0.05, rely=0.9, relx=0.9, anchor="center")
    exit_button.place(relwidth=0.1, relheight=0.05, rely=0.95, relx=0.9, anchor="center")

    window.mainloop()
