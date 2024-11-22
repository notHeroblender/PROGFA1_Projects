courses = ["Programming for artists", "Applied Math and Physics Fundamentals", "Preproduction", "3D1", "Compositing",
           "Programming for artists", "Foundation for film", "Foundation for games", "Compositing", "3D1"]

#clean up and sort list
courses_set = set()
courses_set.update(courses)
courses = list(courses_set)
courses.sort()

for i,course in enumerate(courses):
    print(f"[{i}] {course}")

inpt = int(input("pick one: "))
print(f"You picked {courses[inpt]}")