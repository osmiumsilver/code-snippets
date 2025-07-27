
class StoppableTask implements Runnable {
  private volatile boolean running=true;
  public void stop()
  {
      running=false;
      System.out.println("Stopping task");
  }

    @Override
    public void run() {
        int i=0;
        while(running) {
            i++;
            if (i % 1000000 == 0) {
                System.out.println("Task running... i = " + i);
            }
        }
    }
}

public class testvolatile {
    public static void main(String[] args) throws InterruptedException {
        StoppableTask task = new StoppableTask();
        Thread worker = new Thread(task);
        worker.start();

        Thread.sleep(100); // 让 worker 跑一会

        task.stop(); // 从主线程发出停止信号
        worker.join(); // 等待 worker 线程结束
        System.out.println("Main thread finished.");
    }
}