good =  r"""
         .-~~-.
         (_~..~_)
           ||||
  __________________
 (____    _||||_    )
   ___)  ( _''_ )  (___
  (_      ~-..-~      _)
 ___)                (___
(______          ________)
    ___)        (
   (_____________)
"""
bad = r"""
           .-""-.
           / .--. \
          / /    \ \
          | |    | |
          | |.-""-.|
         ///`.::::.`\
        ||| ::/  \:: ;
        ||; ::\__/:: ;
         \\\ '::::' /
     jgs  `=':-..-'`
"""
has_key = True
if has_key:
   outcome = "Click:The door is open."
   print(good)
else:
   outcome = "Doom:You're trapped."
   print(bad)
print(outcome)
