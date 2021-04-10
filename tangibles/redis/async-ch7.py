from pynput import keyboard

# https://pypi.org/project/pynput/
# https://stackoverflow.com/questions/53088995/pynput-keyboard-listener-does-not-detect-keys-on-mac-os-x
# on Mac, one must go to System Preferences -> Security and Privacy -> Privacy -> 
# Accessibility, and add "Terminal" to "Allow the apps below to control your 
# computer" (if you are running Python or Python3 from Terminal)

def on_press(key):
  try:
    print('alphanumeric key {0} pressed'.format(
      key.char))
  except AttributeError:
    print('special key {0} pressed'.format(
      key))

def on_release(key):
  print('{0} released'.format(
    key))
  if key == keyboard.Key.esc:
    # Stop listener
    return False

# Collect events until released
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
  listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
  on_press=on_press,
  on_release=on_release)
listener.start()

### end ###
