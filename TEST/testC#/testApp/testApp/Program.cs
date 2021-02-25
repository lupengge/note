using System.Net;
using System.IO;
using System;
using Newtonsoft.Json;
using System.Net.Mail;
using Npgsql;
using System.Text;

namespace test
{
    class Program
    {
        static void Main(string[] args)
        {
            //string a = "{\"addTime\":\"2020年12月5日 09:28:06\"}";
            //JsonTest t1 = JsonConvert.DeserializeObject<JsonTest>(a);
            //Console.WriteLine(a);
            //Console.WriteLine(t1.addTime);
            //sendEmail("lupengge@outlook.com", "你好!!!");

            #region commbuider
            //pgsqlTest pgtest = new pgsqlTest();
            //pgtest.testInsert("\"Blogs\"");
            #endregion
            //string html = GetResponse("http://t0.tianditu.gov.cn/img_w/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=img&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles&TILEMATRIX=1&TILEROW=0&TILECOL=0&tk=a85a4e92fc6cbea8f81b6ab4a2e43630", "GET",null);
            //using (StreamWriter writer = new StreamWriter("E:\\test.txt"))
            //{
            //    writer.Write(html);
            //}

            //byte[] file = File.ReadAllBytes("E:\\mysql.txt");
            //Console.WriteLine(file);
            int[] a = {0,1,2,3,4,5,6,7,8,9 };
            Console.WriteLine(chose(a,5));
        }

        static void sendEmail(string receiverAddress, string Message)
        {
            using MailMessage mailMessage = new MailMessage();
            using SmtpClient smtpClient = new SmtpClient("smtp.qq.com", 587);
            mailMessage.To.Add(/*收件人地址*/receiverAddress);
            mailMessage.Body =/*内容*/Message;
            //设置邮件内容是否是 HTML 格式
            mailMessage.IsBodyHtml = true;
            mailMessage.BodyEncoding = System.Text.Encoding.UTF8;
            mailMessage.From = new MailAddress("1739357748@qq.com");
            mailMessage.Subject = "邮件标题";

            smtpClient.EnableSsl = true;
            smtpClient.UseDefaultCredentials = false;
            smtpClient.Credentials = new NetworkCredential("1739357748@qq.com", "wjgzduawjsayddca");
            smtpClient.Send(mailMessage);
        }

        static T[] chose<T>(T[] source, int numRequired)
        {
            T[] result = new T[numRequired];
            int numToChoose = numRequired;
            Random random = new Random();
            for (int numLeft = source.Length; numLeft > 0; numLeft--)
            {
                float prob = (float)numToChoose / (float)numLeft;
                if (random.NextDouble() <= prob)
                {
                    numToChoose--;
                    result[numToChoose] = source[numLeft - 1];
                    if (numToChoose == 0)
                    {
                        break;
                    }
                }
            }
            return result;
        }

        /// <summary>
        /// 向服务器发送请求
        /// </summary>
        /// <param name="url">目标网页地址</param>
        /// <param name="parameters">提交过去的数据没有则可以传空值</param>
        /// <param name="SessionInfo">如果使用Session则输入Session内容，没有可以是任何值</param>
        /// <returns>返回HTML标签语言</returns>
        private static string GetResponse(string url,string method, string SessionInfo = null)
        {
            WebClient client = new WebClient();
            string returnvalue = string.Empty;
            try
            {
                HttpWebRequest Hrequest = (HttpWebRequest)HttpWebRequest.Create(url);
                Hrequest.ContentType = "application/x-www-form-urlencoded";
                //Hrequest.Referer = "";
                Hrequest.Timeout = 600000;
                Hrequest.Method = method;
                //获取登录用户的Session 
                Hrequest.Headers.Add("Cookie", SessionInfo);
                Hrequest.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36");
                Hrequest.Headers.Add("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9");
                Hrequest.Headers.Add("Accept-Encoding", "gzip, deflate");
                Hrequest.Headers.Add("Accept-Language", "zh-CN,zh;q=0.9");
                Hrequest.Headers.Add("Host", "t0.tianditu.gov.cn");
                Hrequest.KeepAlive = true;
                Hrequest.AllowAutoRedirect = true;
                HttpWebResponse Hresponse = (HttpWebResponse) Hrequest.GetResponse();
                
                using (Stream respStream = Hresponse.GetResponseStream())
                {
                    BinaryWriter writer = new BinaryWriter(new FileStream("E:\\test.png",FileMode.Create));
                    
                    int b;
                    while ((b = respStream.ReadByte()) != -1)
                    {
                        writer.Write((byte)b);
                    }
                    writer.Dispose();
                    StreamReader reader = new StreamReader(respStream);
                    
                    returnvalue = reader.ReadToEnd();
                }
                
            }
            catch (Exception exception)
            {
                Console.WriteLine(exception.Message);
            }
            return returnvalue;
        }
    }

    class pgsqlTest
    {
        public string connstring = "Server=127.0.0.1;Port=5432;User ID=postgres;Password=123456;Database=test;";
        public NpgsqlConnection conn = new NpgsqlConnection();
        public pgsqlTest()
        {
            conn.ConnectionString = connstring;
        }
        public pgsqlTest(string connstring)
        {
            this.connstring = connstring;
            conn.ConnectionString = connstring;
        }
        public string testInsert(string tableName)
        {
            string result = "";
            NpgsqlDataAdapter myAdapter = new NpgsqlDataAdapter();

            NpgsqlCommand myCommand = new NpgsqlCommand("select * from " + tableName, conn);
            myAdapter.SelectCommand = myCommand;
            NpgsqlCommandBuilder myCommandBuilder = new NpgsqlCommandBuilder(myAdapter);
            NpgsqlCommand insertComm = myCommandBuilder.GetInsertCommand();
            //NpgsqlParameterCollection a = insertComm.Parameters;
            //a.AddWithValue("@p2","test");
            //a.AddWithValue("@p1",0);
            //conn.Open();
            ////insertComm.ExecuteNonQuery();
            //conn.Close();
            Console.WriteLine(insertComm.CommandText);

            return result;
        }
    }
}
