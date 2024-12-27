import random

from assistant.storage import consistent_storage

def get_name():
    if not consistent_storage.exists('name'):
        return
    else:
        return consistent_storage.get('name')



def done_responses():
    if name := get_name():
        responses = [
            "Okay, Sir!",
            "Done.",
            "All set!",
            "It's completed.",
            "Sure thing!",
            f"Done, {name}!",
            f"All done, {name}.",
            f"Got it, {name}!",
            f"Consider it done, {name}.",
            f"It's taken care of, {name}.",
            f"Ready as you asked, {name}."
        ]
    else:
        responses = [
            "Okay, Sir!",
            "Done.",
            "All set!",
            "It's completed.",
            "Sure thing!",
            "Task completed.",
            "It's all done.",
            "Ready for the next step.",
            "That's finished.",
            "Handled it!"
        ]
    return random.choice(responses)

import random

def error_responses():
    if name:= get_name():
        error_responses = [
            "Something went wrong, Sir.",
            "Error occurred, trying again!",
            f"Apologies, {name}, something's off.",
            f"Couldn't complete the task, {name}.",
            f"An unexpected issue arose, {name}.",
            f"Oops! There's a problem, {name}.",
            f"Sorry, {name}, I encountered an error.",
            "I'm unable to process that right now.",
            "Error: Please check and try again.",
            f"Trouble executing that for you, {name}."
        ]
    else:
        error_responses = [
            "Something went wrong.",
            "Error occurred, trying again!",
            "Apologies, something's off.",
            "Couldn't complete the task.",
            "An unexpected issue arose.",
            "Oops! There's a problem.",
            "Sorry, I encountered an error.",
            "I'm unable to process that right now.",
            "Error: Please check and try again.",
            "Trouble executing that."
        ]
    return random.choice(error_responses)


