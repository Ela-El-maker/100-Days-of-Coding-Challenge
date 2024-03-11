info = (('Monica', 19), ('Tom', 21), ('John', 18))
print("Ascending:",tuple(sorted(info, key=lambda x: x[1])))
print("Descending:",tuple(sorted(info, key=lambda x: x[1], reverse = True)))

