using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MySql.Data.MySqlClient;

namespace Data_Loader
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            MySqlConnection conn = DBUtils.GetDBConnection();
            try
            {
                conn.Open();
                //MessageBox.Show("Connection - OK");
                string Query = "SELECT * FROM `" + textBox1.Text[0] + textBox1.Text[1] + "` WHERE `combos` LIKE '%" + textBox1.Text + "%'";
                MySqlCommand cmd = new MySqlCommand(Query, conn);
                cmd.CommandTimeout = 60;
                MySqlDataReader reader;
                reader = cmd.ExecuteReader();
                var list = new List<string>();
                if (reader.HasRows)
                {
                    int counter = 0;
                    while (reader.Read())
                    {
                        listBox1.Items.Add(reader["combos"].ToString());
                    }
                    conn.Close();
                 }
                else
                {
                    MessageBox.Show("Nothing found");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error - " + ex.Message);
            }

        }


        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            textBox2.Text = listBox1.SelectedItem.ToString();
            textBox3.Text = listBox1.SelectedItem.ToString().Split(':')[0];
            textBox4.Text = listBox1.SelectedItem.ToString().Split(':')[1];
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            MySqlConnection conn = DBUtils.GetDBConnection();
            try
            {
                conn.Open();
                //MessageBox.Show("Connection - OK");
                string Query = "SELECT SUM(TABLE_ROWS) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'crew_db';";
                MySqlCommand cmd = new MySqlCommand(Query, conn);
                MySqlDataReader reader;
                reader = cmd.ExecuteReader();
                if (reader.Read())
                {
                    label5.Text = "Lines in base -> " + reader.GetString(0).ToString();
                }
                conn.Close();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error - " + ex.Message);
            }
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            //textBox2.Text = listBox1.SelectedItem.ToString();
        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {
        }
    }
}
