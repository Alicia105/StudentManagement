from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///studentManagement.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)# Primary key but no auto-increment
    course_id = db.Column(db.String(10), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.String(10), unique=True)
    name = db.Column(db.String(100), nullable=False)
    prof_name = db.Column(db.String(100), nullable=False)
    credit_hours = db.Column(db.Integer, nullable=False)
    number_of_students = db.Column(db.Integer, nullable=False)
    max_number_of_students = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.String(20), nullable=False)

student_courses = db.Table('student_courses',
    db.Column('student_id', db.String(100), db.ForeignKey('student.student_id'), primary_key=True),
    db.Column('course_id', db.String(10), db.ForeignKey('course.course_id'), primary_key=True)
)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)# Primary key but no auto-increment
    student_id = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    major = db.Column(db.String(100), nullable=False)
    courses = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.String(100), nullable=False)
    courses = db.relationship('Course', secondary=student_courses, backref='students')

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)# Primary key but no auto-increment
    admin_id = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.String(100), nullable=False)
    mail = db.Column(db.String(100), nullable=False)
    job_position= db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()

@app.route('/')
def welcome():
    return "Bienvenue !"

#GET all courses
@app.route('/courses',methods=['GET'])
def get_courses():
    courses=Course.query.all()
    return jsonify([{'course Name': c.name,
                     'ID': c.course_id,
                     'Number of students':c.number_of_students,
                     'Max Number of students': c.max_number_of_students,
                     'semester': c.semester, 'number of credit hours': c.credit_hours,
                     'Professor Name': c.prof_name} for c in courses])

#GET a specific course
@app.route('/courses/<string:course_id>',methods=['GET'])
def get_course(course_id):
   
    c= Course.query.filter_by(course_id=course_id.upper()).first()

    if c:
        return jsonify({'course Name': c.name,
                        'ID': c.course_id,
                        'Number of students':c.number_of_students,
                        'Max Number of students': c.max_number_of_students,
                        'semester': c.semester, 'number of credit hours': c.credit_hours,
                        'Professor Name': c.prof_name})

    return jsonify({"error": "Course not found"}),404

#DELETE a specific course
@app.route('/courses/<string:course_id>', methods=['DELETE'])
def delete_course(course_id):
    c = Course.query.filter_by(course_id=course_id.upper()).first()

    if not c :
        return jsonify({"error": "Course not found"}),404
    db.session.delete(c)
    db.session.commit()

    return jsonify({"message": "Course deleted"}),200

#POST a specific course
@app.route('/courses',methods=['POST'])
def add_course():
    data=request.get_json()

    if not data or "course Name" not in data or "ID" not in data:
        return jsonify({"error": "Invalid input"}),400

    # Check if course already exists
    existing_course = Course.query.filter_by(course_id=data["ID"].upper()).first()
    if existing_course:
        return jsonify({"error": "Course ID already exists"}), 409  # Conflict

    new_course=Course(
        course_id=data["ID"].upper(),
        name=data["course Name"],
        prof_name=data["Professor Name"],
        credit_hours=data["number of credit hours"] ,
        number_of_students=data.get("Number of students", 0),  # Default to 0
        max_number_of_students=data["Max Number of students"] ,
        semester=data["semester"]
    )

    db.session.add(new_course)
    db.session.commit()

    return jsonify({"meassage": "Course added successfully",
                    "course":{
                        'course Name': new_course.name,
                        'ID': new_course.course_id,
                        'Number of students':new_course.number_of_students,
                        'Max Number of students': new_course.max_number_of_students,
                        'semester': new_course.semester,
                        'number of credit hours': new_course.credit_hours,
                        'Professor Name': new_course.prof_name
                        }
                    }),201

#PUT a specific course
@app.route('/courses/<string:course_id>',methods=['PUT'])
def update_course(course_id):

    data=request.get_json()

    if not data:
        return jsonify({"error": "Invalid input"}),400
    
    course = Course.query.filter_by(course_id=course_id.upper()).first()


    if not course :
        return jsonify({"error": "Course not found"}),404
    
    course.name=data.get("course Name",course.name)
    course.course_id=data.get("ID",course.course_id)
    course.number_of_students=data.get("Number of students",course.number_of_students)
    course.max_number_of_students=data.get("Max Number of students",course.max_number_of_students)
    course.semester=data.get("semester",course.semester)
    course.credit_hours=data.get("number of credit hours",course.credit_hours)
    course.prof_name=data.get("Professor Name",course.prof_name)
   
    db.session.commit()
   
    return jsonify({"meassage": "Course updated successfully",
                    "course":{
                        'course Name': course.name,
                        'ID': course.course_id,
                        'Number of students':course.number_of_students,
                        'Max Number of students': course.max_number_of_students,
                        'semester': course.semester,
                        'number of credit hours': course.credit_hours,
                        'Professor Name': course.prof_name
                        }
                    }),200

#---------------------------------------------------------------------------------------------
"""students=[{'name': 'John','lastName': 'Doe',
            'age': 25, 'dateOfBirth': '20/01/2000',
            'major': 'M.Sc EE', 'courses': [],
            'id': 'A175', 'mail': 'jdoe@school.edu',
            'password': b'QVpFUg=='}]
"""

#GET all students
@app.route('/students',methods=['GET'])
def get_students():
    students=Student.query.all()
    return jsonify([{'name': s.name,
                     'lastName': s.last_name,
                     'id': s.student_id,
                     'mail':s.mail,
                     'password': s. password,
                     'major': s. major, 'age': s.age,
                     'dateOfBirth': s. date_of_birth } for s in students])

#GET a specific student
@app.route('/students/<string:student_id>',methods=['GET'])
def get_student(student_id):
   
    s= Student.query.filter_by(student_id=student_id.upper()).first()

    if s:
        return jsonify({'name': s.name,
                     'lastName': s.last_name,
                     'id': s.student_id,
                     'mail':s.mail,
                     'password': s. password,
                     'major': s. major, 'age': s.age,
                     'dateOfBirth': s. date_of_birth})

    return jsonify({"error": "Student not found"}),404

#DELETE a specific student
@app.route('/students/<string:student_id>', methods=['DELETE'])
def delete_student(student_id):
    s = Student.query.filter_by(student_id=student_id.upper()).first()

    if not s :
        return jsonify({"error": "Student not found"}),404
    db.session.delete(s)
    db.session.commit()

    return jsonify({"message": "Student deleted"}),200

#POST a specific student
@app.route('/students',methods=['POST'])
def add_student():
    data=request.get_json()

    if not data or "name" not in data or "id" not in data:
        return jsonify({"error": "Invalid input"}),400

    # Check if student already exists
    existing_student = Student.query.filter_by(student_id=data["id"].upper()).first()
    if existing_student:
        return jsonify({"error": "Student ID already exists"}), 409  # Conflict

    new_student = Student(
    name=data["name"],
    last_name=data["lastName"],
    student_id=data["id"].upper(),
    mail=data["mail"],
    password=data["password"],
    major=data["major"],
    age=data.get("age", 0),
    date_of_birth=data["dateOfBirth"]
    )
   
    db.session.add(new_student)
    db.session.commit()

    return jsonify({
    "message": "Student added successfully",
    "student": {
        'name': new_student.name,
        'lastName': new_student.last_name,
        'id': new_student.student_id,
        'mail': new_student.mail,
        'major': new_student.major,
        'age': new_student.age,
        'dateOfBirth': new_student.date_of_birth,
        'password': new_student.password
    }}), 201

#PUT a specific student
@app.route('/students/<string:student_id>',methods=['PUT'])
def update_student(student_id):

    data=request.get_json()

    if not data:
        return jsonify({"error": "Invalid input"}),400
    
    student= Student.query.filter_by(student_id=student_id.upper()).first()

    if not student :
        return jsonify({"error": "student not found"}),404
    
    student.name=data.get("name",student.name)
    student.student_id=data.get("id",student.student_id)
    student.last_name=data.get("lastName",student.last_name)
    student.mail=data.get("mail",student.mail)
    student.password=data.get("password",student.password)
    student.major=data.get("major",student.major)
    student.date_of_birth=data.get("dateOfBirth",student.date_of_birth)
    student.age=data.get("age",student.age)

    db.session.commit()
   
    return jsonify({
    "message": "Student updated successfully",
    "student": {
        'name': student.name,
        'lastName': student.last_name,
        'id': student.student_id,
        'mail': student.mail,
        'major': student.major,
        'age': student.age,
        'dateOfBirth': student.date_of_birth,
        'password': student.password,
    }
    }), 200

#---------------------------------------------------------------------------------------------
"""admin={'name': 'Alan',
         'lastName': 'Doe', 'dateOfBirth': '20/01/2000',
         'job position': 'Professor', 'startDate': '09/2023',
         'id': 'S214', 'mail': 'adoe@school.edu', 'password': b'QVpFUg=='}"""



#GET all admins
@app.route('/admins',methods=['GET'])
def get_admins():
    admins=Admin.query.all()
    return jsonify([{'name': s.name,
                     'lastName': s.last_name,
                     'id': s.admin_id,
                     'mail':s.mail,
                     'password': s.password,
                     'startDate': s.start_date,
                     'dateOfBirth': s.date_of_birth,
                     'job position':s.job_position } for s in admins])

#GET a specific admin
@app.route('/admins/<string:admin_id>',methods=['GET'])
def get_admin(admin_id):
   
    s= Admin.query.filter_by(admin_id=admin_id.upper()).first()

    if s:
        return jsonify({'name': s.name,
                     'lastName': s.last_name,
                     'id': s.admin_id,
                     'mail':s.mail,
                     'password': s.password,
                     'startDate': s.start_date,
                     'dateOfBirth': s.date_of_birth,
                      'job position':s.job_position })

    return jsonify({"error": "Admin not found"}),404

#DELETE a specific admin
@app.route('/admins/<string:admin_id>', methods=['DELETE'])
def delete_admin(admin_id):
    s = Admin.query.filter_by(admin_id=admin_id.upper()).first()

    if not s :
        return jsonify({"error": "Admin not found"}),404
    db.session.delete(s)
    db.session.commit()

    return jsonify({"message": "Admin deleted"}),200

#POST a specific admin
@app.route('/admins',methods=['POST'])
def add_admin():
    data=request.get_json()

    if not data or "name" not in data or "id" not in data:
        return jsonify({"error": "Invalid input"}),400

    # Check if admin already exists
    existing_admin = Admin.query.filter_by(admin_id=data["id"].upper()).first()
    if existing_admin:
        return jsonify({"error": "Admin ID already exists"}), 409  # Conflict

    new_admin = Admin(
        name=data["name"],
        last_name=data["lastName"],
        admin_id=data["id"].upper(),
        mail=data["mail"],
        password=data["password"],
        start_date=data["startDate"],      
        date_of_birth=data["dateOfBirth"],
        job_position=data['job position']
    )

    db.session.add(new_admin)
    db.session.commit()

    return jsonify({
    "message": "Admin added successfully",
    "admin": {      'name': new_admin.name,
                     'lastName': new_admin.last_name,
                     'id': new_admin.admin_id,
                     'mail':new_admin.mail,
                     'password': new_admin.password,
                     'startDate': new_admin.start_date,
                     'dateOfBirth': new_admin.date_of_birth,
                     'job position':new_admin.job_position 
    }}), 201

#PUT a specific admin
@app.route('/admins/<string:admin_id>',methods=['PUT'])
def update_admin(admin_id):

    data=request.get_json()

    if not data:
        return jsonify({"error": "Invalid input"}),400
    
    admin= Admin.query.filter_by(admin_id=admin_id.upper()).first()

    if not admin :
        return jsonify({"error": "admin not found"}),404
    
    admin.name=data.get("name",admin.name)
    admin.admin_id=data.get("id",admin.admin_id)
    admin.last_name=data.get("lastName",admin.last_name)
    admin.mail=data.get("mail",admin.mail)
    admin.password=data.get("password",admin.password)
    admin.start_date=data.get("startDate",admin.start_date)
    admin.date_of_birth=data.get("dateOfBirth",admin.date_of_birth)
    admin.job_position=data.get("job position",admin.job_position)

    db.session.commit()
   
    return jsonify({
    "message": "admin updated successfully",
    "admin": {
        'name': admin.name,
         'lastName': admin.last_name,
                     'id': admin.admin_id,
                     'mail':admin.mail,
                     'password': admin.password,
                     'startDate': admin.start_date,
                     'dateOfBirth': admin.date_of_birth,'job position':admin.job_position 
    }
    }), 200
   

if __name__=="__main__":
    app.run(debug=True)


