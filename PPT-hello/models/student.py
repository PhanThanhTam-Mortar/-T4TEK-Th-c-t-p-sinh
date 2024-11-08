
from odoo import fields, models

class StudentOdoo(models.Model):
    _name = 'student.odoo'
    _description = 'Học viên'

    name = fields.Char(string='Tên học viên', required=True)
    age = fields.Integer(string='Tuổi', help='Tuổi của học viên')
    sex = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác')
    ], string='Giới tính', help='Giới tính của học viên')
    date_of_birth = fields.Date(string='Ngày sinh', help='Ngày tháng năm sinh của học viên')
    image = fields.Binary(string='Hình ảnh', help='Hình ảnh của học viên')
    
    # Trường student_id sử dụng sequence
    student_id = fields.Char(
        string='Mã học viên',
        required=True,
        readonly=True,
        copy=False,
        default=lambda self: self.env['ir.sequence'].next_by_code('student.odoo') or 'HV0000',
        help='Mã học viên duy nhất'
    )
    
    address = fields.Text(string='Địa chỉ', help='Địa chỉ của học viên')
    phone = fields.Char(string='Số điện thoại', help='Số điện thoại liên lạc của học viên')
    email = fields.Char(string='Email', help='Email của học viên') 
    
    # Trường trạng thái
    status = fields.Selection([
        ('waiting', 'Chờ xét duyệt'),
        ('in_progress', 'Đang học'),
        ('absent', 'Vắng mặt'),
        ('completed', 'Hoàn thành'),
    ], string="Trạng thái học viên", default='waiting', help="Trạng thái hiện tại của học viên")

