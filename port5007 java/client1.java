package Client_1;
import java.io.BufferedOutputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;

public class Client1 {
    public static final int SOCKET_PORT = 5007;
    public static final String SERVER = "localhost";
    public static final String FILE_TO_RECEIVE = "TextFile_received_1.txt";

    public static void main(String[] args) throws IOException {
        int bytesRead;
        int current = 0;
        FileOutputStream fos = null;
        BufferedOutputStream bos = null;
        Socket sock = null;

        try {
            sock = new Socket(SERVER, SOCKET_PORT);
            System.out.println("Connected...");

          
            byte[] mybytearray = new byte[1024];
            InputStream is = sock.getInputStream();
            fos = new FileOutputStream(FILE_TO_RECEIVE);
            bos = new BufferedOutputStream(fos);

           
            int fileSize = is.read(mybytearray);

            do {
                bytesRead = is.read(mybytearray, current, (mybytearray.length - current));
                if (bytesRead >= 0) {
                    current += bytesRead;
                }
            } while (current < fileSize);

            bos.write(mybytearray, 0, current);
            bos.flush();

            System.out.println("File " + FILE_TO_RECEIVE + " downloaded (" + current + " bytes read)");

        } finally {
            if (fos != null) {
                fos.close();
            }
            if (bos != null) {
                bos.close();
            }
            if (sock != null) {
                sock.close();
            }
        }
    }
}
//please dont edit these codess