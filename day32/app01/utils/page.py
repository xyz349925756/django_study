#!/usr/bin/python3
# -*-coding:utf-8-*-
# Auth: xyz34
# File: page.py
# TIME: 2022/10/8 星期六  周六


class Pagination(object):

    def __init__(self, current_page, all_count, per_page_num=10, pager_count=11):
        """
        封装分页相关数据
        @param current_page: 当前页
        @param all_count:    所有页
        @param per_page_num: 每页显示数据条数
        @param pager_count:  最多显示的页码数
        """
        try:
            current_page = int(current_page)
        except Exception as e:
            current_page = 1
        # 上面把获取到的get page 转为int型,

        # current_page不能为负数
        if current_page < 1:
            current_page = 1

        self.current_page = current_page
        self.all_count = all_count
        self.per_page_num = per_page_num

        all_pager, tmp = divmod(all_count, per_page_num)
        if tmp:
            all_pager += 1

        self.all_pager = all_pager
        self.pager_count = pager_count
        self.pager_count_half = int((pager_count - 1) / 2)

    @property  # 只读属性
    def start(self):
        return (self.current_page - 1) * self.per_page_num

    @property
    def end(self):
        return self.current_page * self.per_page_num

    def page_html(self):

        if self.all_pager <= self.pager_count:  # 如果当前页码小于11
            pager_start = 1
            pager_end = self.pager_count + 1
        else:  # >11
            if self.current_page <= self.pager_count_half:
                pager_start = 1
                pager_end = self.pager_count + 1
            else:
                if (self.current_page + self.pager_count_half) > self.all_pager:
                    pager_end = self.all_pager + 1
                    pager_start = self.all_pager - self.pager_count + 1
                else:
                    pager_start = self.current_page - self.pager_count_half
                    pager_end = self.current_page + self.pager_count_half + 1

        page_html_list = []
        page_html_list.append('''
           <nav aria-label="..." class="d-flex justify-content-center">
             <ul class="pagination">
        ''')
        first_page = f'<li class="page-item"><a aria-label="Previous" class="page-link" href="?page=1"><span aria-hidden="true">首页</span></a></li>'
        page_html_list.append(first_page)

        if self.current_page <= 1:
            prev_page = f'<li class="page-item disabled"><a aria-label="Previous" class="page-link" href="?page={self.current_page - 1}"><span aria-hidden="true">上一页</span></a></li>'
        else:
            prev_page = f'<li class="page-item"><a aria-label="Previous" class="page-link" href="?page={self.current_page - 1}"><span aria-hidden="true">上一页</span></a></li>'

        page_html_list.append(prev_page)

        for i in range(pager_start, pager_end):
            if i == self.current_page:
                tmp = f'<li class="page-item active" aria-current="page"><a class="page-link" href="?page={i}">{i}</a></li>'
            else:
                tmp = f'<li class="page-item" aria-current="page"><a class="page-link" href="?page={i}">{i}</a></li>'
            page_html_list.append(tmp)

        if self.current_page >= self.all_pager:
            next_page = f'<li class="page-item disabled"><a aria-label="Next" class="page-link" href="?page={self.current_page + 1}"><span aria-hidden="true">下一页</span></a></li>'
        else:
            next_page = f'<li class="page-item"><a aria-label="Next" class="page-link" href="?page={self.current_page + 1}"><span aria-hidden="true">下一页</span></a></li>'
        page_html_list.append(next_page)

        last_page = f'<li class="page-item"><a aria-label="Previous" class="page-link" href="?page={self.all_pager}"><span aria-hidden="true">尾页</span></a></li>'
        page_html_list.append(last_page)

        page_html_list.append('''
                </ul>
            </nav>
        ''')
        return ''.join(page_html_list)