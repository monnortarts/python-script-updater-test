import updater_interfacer

updater_interfacer.version = 0

input(f"Newest Version: {updater_interfacer.get_latest_version()}\nCurrent Version: {updater_interfacer.version}\nPress Enter to update.")
updater_interfacer.update()