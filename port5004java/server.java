import java.io.*;
import java.net.*;

public class server {
    public static void main(String var[]) {
        try {
            ServerSocket ss = new ServerSocket(5004);
            Socket s = ss.accept();

            DataInputStream dis = new DataInputStream(s.getInputStream());
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String str2 =  " ";

            while(!str2.equals("bye")) {

                String str1 = (String)dis.readUTF();
                System.out.println("Client : " + str1);
                str2 = br.readLine();
                dout.writeUTF(str2);
            }
            
            s.close();
            ss.close();
            dis.close();
            dout.close();
        }
        catch(Exception e) {
            System.out.println(e);
        }
    }
    
}
