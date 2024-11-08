import logging
from odoo import http
from odoo.http import request
from werkzeug.utils import redirect

_logger = logging.getLogger(__name__)

class MainController(http.Controller):

    # Route 1: Hiển thị danh sách khóa học
    @http.route('/courses', type='http', auth="public", website=True)
    def get_courses(self):
        # Lấy danh sách tất cả các khóa học từ model 'course.odoo'
        records = request.env['course.odoo'].search([])

        # Render trang HTML và truyền biến "courses" cho template
        return request.render(
            "your_module.course_list_template",  # Tên của template sẽ được sử dụng
            {
                "courses": records,  # Truyền dữ liệu khóa học vào template
            },
        )
    
    # Route 2: Xem chi tiết một khóa học
    @http.route('/courses/<int:course_id>', type='http', auth="public", website=True)
    def view_course(self, course_id):
        # Tìm khóa học theo ID
        course = request.env['course.odoo'].sudo().browse(course_id)
        
        # Kiểm tra xem khóa học có tồn tại hay không
        if not course.exists():
            return redirect('/courses')
        
        # Render template chi tiết khóa học
        return request.render(
            "your_module.course_detail_template",  # Tên template chi tiết
            {
                "course": course,  # Truyền dữ liệu khóa học vào template
            },
        )

    # Route 3: Thêm khóa học mới
    @http.route('/courses/add', type='http', auth="user", website=True)
    def add_course(self, **post):
        # Kiểm tra nếu có dữ liệu được gửi lên từ form
        if post:
            # Tạo bản ghi khóa học mới từ dữ liệu trong form
            request.env['course.odoo'].create({
                'name': post.get('name'),
                'description': post.get('description'),
                'teacher': post.get('teacher'),
                'price': post.get('price'),
            })
            return redirect('/courses')  # Quay lại danh sách khóa học

        # Nếu không có dữ liệu từ form, hiển thị form thêm khóa học
        return request.render(
            "your_module.course_add_template",  # Tên template để hiển thị form
            {},
        )

    # Route 4: Cập nhật thông tin khóa học
    @http.route('/courses/edit/<int:course_id>', type='http', auth="user", website=True)
    def edit_course(self, course_id, **post):
        # Lấy khóa học cần sửa
        course = request.env['course.odoo'].sudo().browse(course_id)
        
        if not course.exists():
            return redirect('/courses')
        
        # Nếu có dữ liệu gửi lên từ form, cập nhật thông tin khóa học
        if post:
            course.write({
                'name': post.get('name'),
                'description': post.get('description'),
                'teacher': post.get('teacher'),
                'price': post.get('price'),
            })
            return redirect('/courses')  # Quay lại danh sách khóa học
        
        # Nếu không có dữ liệu từ form, hiển thị form chỉnh sửa
        return request.render(
            "your_module.course_edit_template",  # Tên template để hiển thị form chỉnh sửa
            {
                'course': course,  # Truyền dữ liệu khóa học vào form
            },
        )
