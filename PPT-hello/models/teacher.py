# -*- coding: utf-8 -*-
from odoo import fields, models

class TeacherOdoo(models.Model):
    _name = 'teacher.odoo'
    _description = 'Giảng viên'

    name = fields.Char(string='Tên giảng viên', required=True)
    age = fields.Integer(string='Tuổi', help='Tuổi của giảng viên')
    sex = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác')
    ], string='Giới tính', help='Giới tính của giảng viên')

    date_of_birth = fields.Date(string='Ngày sinh', help='Ngày tháng năm sinh của giảng viên')
    image = fields.Binary(string='Hình ảnh', help='Hình ảnh của giảng viên')  # Hình ảnh giảng viên dưới dạng nhị phân (binary)
    employee_id = fields.Char(string='Mã giảng viên', required=True, help='Mã giảng viên duy nhất', readonly=True, copy=False, default=lambda self: self.env['ir.sequence'].next_by_code('teacher.odoo') or 'GV0000')
    address = fields.Text(string='Địa chỉ', help='Địa chỉ của giảng viên')
    phone = fields.Char(string='Số điện thoại', help='Số điện thoại liên lạc của giảng viên')
    email = fields.Char(string='Email', help='Email của giảng viên')
    department = fields.Char(string='Khoa', help='Khoa mà giảng viên đang công tác')
    qualification = fields.Char(string='Trình độ chuyên môn', help='Trình độ học vấn của giảng viên')
    hire_date = fields.Date(string='Ngày vào làm', help='Ngày giảng viên bắt đầu công tác')
