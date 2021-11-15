class Garden:
    """Given a diagram, return which plants each child is responsible for."""
    STUDENTS = [
        'Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
        ]
          

    FLOWERS = {
        'C': 'Clover',
        'V': 'Violets',
        'R': 'Radishes',
        'G': 'Grass'
    }


    def __init__(self, diagram, students=STUDENTS):
        self.diagram = diagram
        self.students = students
        self.indices = {v: i for i, v in enumerate(sorted(students))}


    def part(self):
        return self.diagram.split('\n')


    def plants(self, student):
        s = ''
        parts = self.part()
        for i in range(len(parts)):
            s += parts[i][self.indices[student] * 2: (self.indices[student] * 2) + 2]
        return [self.FLOWERS[x] for x in s] 
