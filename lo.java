public class lo {
  static String formatLength(String text) {
    if (text != null) {
      return "Text length: " + text.length();
    } else {
      return "Text is null";
    }
  }
  public static void main(String[] args) {

  
  
  String message = null;
  String formattedMessage = formatLength(message); 
  int length = formattedMessage.length();
  System.out.println(length);
    }
}
