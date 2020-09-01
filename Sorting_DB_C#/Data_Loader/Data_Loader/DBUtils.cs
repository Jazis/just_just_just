using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MySql.Data.MySqlClient;

namespace Data_Loader
{
    class DBUtils
    {
        public static MySqlConnection GetDBConnection()
        {
            string host = "192.168.1.3";
            int port = 3306;
            string database = "crew_db";
            string username = "Jazis";
            string password = "1234567890";

            return DBMySQLUtils.GetDBConnection(host, port, database, username, password);
        }

    }
}