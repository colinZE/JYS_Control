# -*- coding: utf-8 -*-
__author__ = 'Administrator'
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from CMDB import models
class Pagination(object):
    def __init__(self):
        pass

    @classmethod
    def create_pagination(self,articles_list,page="",one_page_data_size=10,show_page_item_len=5):
        """
        :param page: 当前页码
        :param one_page_data_size: 每一页显示几行
        :param show_page_item_len: 显示几个能点击的页数
        :return:

        """


        #查询所需要的数据对象

        # articles_list = models.ServerInfo.objects.all()
        print("pagination",page)
        print("articles_list",articles_list,type(articles_list))
        #根据查询到的数据创建分页实例对象
        paginator = Paginator(articles_list, one_page_data_size)
        print("元素数量",paginator.count)
        print("页数",paginator.num_pages)
        print("取第一页分页对象",paginator.page(1))
        print("列出第一页元素",paginator.page(1).object_list)
        try:
            current_page = paginator.page(page)
            print("current_page",current_page)
            articles = current_page.object_list
        except PageNotAnInteger:
            current_page = paginator.page(1)
            articles = current_page.object_list

        #计算总页数
        all_page = current_page.paginator.num_pages
        print("page_all",all_page)

        #计算显示的最小页

        # print("1/2",show_page_item_len/2,type(show_page_item_len/2),float(page),type(page))
        start_page = float(page) - show_page_item_len/2
        if start_page > all_page - show_page_item_len:
            start_page = all_page - show_page_item_len + 1
        if start_page < 1:
            start_page = 1
        else:
            start_page=start_page

        #计算显示的最大页
        end_page = float(page) + show_page_item_len/2
        print("end_page1",end_page,"all_page",all_page)
        if end_page > all_page:
            end_page = all_page
        else:
            end_page=end_page
        if end_page < show_page_item_len and all_page >= show_page_item_len:
            end_page = show_page_item_len

        #生成能点击的展示码
        print("page_jisuan",start_page,end_page,int(end_page),"all_page",all_page,page)
        page_items = range(start_page,int(end_page) + 1)
        print("page_2222",start_page,int(end_page)+1)
        print("range",range(1,5))

        pagination_dic = {
            'current_page': current_page,
            'articles': articles,
            'page_all': all_page,
            # 'start_page': start_page,
            # 'end_page': end_page,
            'page_items': page_items,
        }
        return pagination_dic
