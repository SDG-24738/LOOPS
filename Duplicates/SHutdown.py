def shutdown(saved, running):
    if saved == "no" or running == "no":
        print("abort shutdown")
    elif saved == "Yes" and running == "Yes":
        print("Shutdown")
    else:
        print("sorry")
saved = input("unsaved programs exist is it okay to shut down")
running = input("some programs are still running exist is it okay to shut down")
shutdown(saved, running)