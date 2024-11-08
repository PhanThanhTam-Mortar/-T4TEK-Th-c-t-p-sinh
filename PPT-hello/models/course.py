from odoo import fields, models

class CourseOdoo(models.Model):
    _name = 'course.odoo'
    _description = 'Khóa học'

    name = fields.Char(string='Tên khóa học', required=True)
    code = fields.Char(string='Mã khóa học', required=True, help='Mã khóa học duy nhất')
    description = fields.Text(string='Mô tả', help='Mô tả chi tiết về khóa học')
    start_date = fields.Date(string='Ngày bắt đầu', help='Ngày bắt đầu khóa học')
    end_date = fields.Date(string='Ngày kết thúc', help='Ngày kết thúc khóa học')
    instructor_ids = fields.Many2many('teacher.odoo', string='Giảng viên', help='Danh sách giảng viên tham gia khóa học')
    student_ids = fields.Many2many('student.odoo', string='Học viên', help='Danh sách học viên tham gia khóa học')
    schedule_ids = fields.One2many('schedule.odoo', 'course_id', string='Lịch học')
