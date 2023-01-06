using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace HighChartsJavaScript
{
    public partial class Default : System.Web.UI.Page
    {
        const int ComboChartBarGroups = 5;    //max bars to display
        protected string[] xAxisFruit = new string[ComboChartBarGroups];
        protected int[] userJane = new int[ComboChartBarGroups];
        protected int[] userJohn = new int[ComboChartBarGroups];
        protected int[] userJoe = new int[ComboChartBarGroups];

        protected void Page_Load(object sender, EventArgs e)
        {
            //SqlDatabase Database = new SqlDatabase(ConfigurationManager.ConnectionStrings
            //                                                ["ConnectionString"].ToString());
            /////initialize Combo chart 
            /////--------------------
            /////Start by reading in the values from the DB
            //DbCommand MyCommand = Database.GetStoredProcCommand("GetTopProjectServiceOrders");
            //Database.AddInParameter(MyCommand, "@user_name_", DbType.String, Session["user_name_"].ToString());
            //Database.AddInParameter(MyCommand, "@period_", DbType.Int32, DefaultTimeInMonths);

            //dataReader = Database.ExecuteReader(MyCommand);

            //_cntr = 0;
            //while (dataReader.Read()&& _cntr < ComboChartBarGroups) 
            //{
            //    xAxisFruit[_cntr] = dataReader["project_name_"].ToString();
            //    userJane[_cntr] = Convert.ToInt32(dataReader["open_so_count_"]);
            //    userJohn[_cntr] = Convert.ToInt32(dataReader["closed_so_count_"]);
            //    userJoe[_cntr] = Convert.ToInt32(dataReader["past_due_so_count_"]);
            //    _cntr++;
            //}

            xAxisFruit[0] = "Apples";  
            userJane[0] = 3;
            userJohn[0] = 2;
            userJoe[0] = 4;

            xAxisFruit[1] = "Oranges";
            userJane[1] = 2;
            userJohn[1] = 3;
            userJoe[1] = 3;

            xAxisFruit[2] = "Pears";
            userJane[2] = 1;
            userJohn[2] = 5;
            userJoe[2] = 3;

            xAxisFruit[3] = "Bananas";
            userJane[3] = 3;
            userJohn[3] = 7;
            userJoe[3] = 9;

            xAxisFruit[4] = "Plums";
            userJane[4] = 4;
            userJohn[4] = 6;
            userJoe[4] = 0;
        }
    }
}