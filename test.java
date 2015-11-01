import java.io.FileNotFoundException;
import java.io.IOException;

import com.csvreader.CsvReader;

public class test {

	public static void main(String[] args) {
		try {
			
			CsvReader test = new CsvReader("test.csv");
		
			test.readHeaders();

			while (test.readRecord())
			{
				// perform program logic here
				System.out.println(test.get());
			}
	
			test.close();
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}

}