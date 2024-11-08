{
    'name': 'Quản lý trung tâm tiếng anh',
    'version': '1.0',
    'category': 'Education',
    'description': 'Quản lý học viên, giảng viên, khóa học và lịch học',

    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',  # Cấu hình quyền truy cập
        #'views/course_list_template.xml',
        'data/student_sequence.xml',
        'data/teacher_sequence.xml',
        #'views/student1_views.xml',
        'views/student_views.xml',  # Đảm bảo đường dẫn đúng đến tệp XML
        'views/teacher_views.xml',
        'views/course_views.xml',
        'views/schedule_view.xml',



    ],
    'installable': True,
    'application': True,  
    'auto_install': False, 


}
