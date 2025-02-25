import updater_interfacer

input(f"Newest Version: {updater_interfacer.get_latest_release_info('version')}\nRelease notes: \n{updater_interfacer.get_latest_release_info('notes')}\nCurrent Version: {updater_interfacer.version}\nPress Enter to update.")
updater_interfacer.update()
