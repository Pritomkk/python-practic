﻿using System.Web;
using System.Web.Mvc;

namespace Class_Task_validation_
{
    public class FilterConfig
    {
        public static void RegisterGlobalFilters(GlobalFilterCollection filters)
        {
            filters.Add(new HandleErrorAttribute());
        }
    }
}
