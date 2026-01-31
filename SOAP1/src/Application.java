import javax.xml.ws.Endpoint;

public class Application {
    public static void main(String[] args) {
        System.out.println("Début de deploiement de mon ");
        String url = "http://localhost:8888/";
        Endpoint.publish(url, new MonServiceWeb());
        System.out.println("Le service web est bien deployé");
    }
}
