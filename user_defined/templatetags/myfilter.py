#_*_ coding:utf-8 _*_

from django import template

register = template.Library()

#声明并定义过滤器

@register.filter
def myreplace(value,args):
    oldValue = args.split(':')[0]
    newValue = args.split(':')[1]
    return value.replace(oldValue,newValue)