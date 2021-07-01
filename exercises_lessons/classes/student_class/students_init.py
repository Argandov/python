#!/usr/bin/python3


from students import Students as s

courses = ["ASM", "lua"]
write = s("john", "hammond", courses)
write.checker()

john_courses = ["python", "ruby"]
write = s("john", "doe", john_courses)
print(write.check_if_exists())
