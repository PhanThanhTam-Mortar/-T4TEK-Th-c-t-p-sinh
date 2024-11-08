from odoo import fields, models

class ScheduleOdoo(models.Model):
    _name = 'schedule.odoo'
    _description = 'Lịch học'

    name = fields.Char(string='Tên lịch học', required=True)
    course_id = fields.Many2one('course.odoo', string='Khóa học', required=True)
    instructor_id = fields.Many2one('teacher.odoo', string='Giảng viên', required=True)
    date = fields.Date(string='Ngày học', required=True)
    start_time = fields.Float(string='Giờ bắt đầu', required=True)
    end_time = fields.Float(string='Giờ kết thúc', required=True)
    room = fields.Char(string='Phòng học', help='Phòng học nơi diễn ra buổi học')
    student_ids = fields.Many2many('student.odoo', string='Học viên', help='Danh sách học viên tham gia buổi học')
