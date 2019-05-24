package config;

import java.io.*; 
import java.util.*;

import edu.cmu.sphinx.api.Configuration;
import edu.cmu.sphinx.api.SpeechResult;
import edu.cmu.sphinx.api.StreamSpeechRecognizer;

public class Config {       

    public static void main(String[] args) throws Exception {
    	 ArrayList<String> words = new ArrayList<String>();
        Configuration configuration = new Configuration();

        configuration.setAcousticModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us");
        configuration.setDictionaryPath("resource:/edu/cmu/sphinx/models/en-us/cmudict-en-us.dict");
        configuration.setLanguageModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us.lm.bin");

	StreamSpeechRecognizer recognizer = new StreamSpeechRecognizer(configuration);
	InputStream stream = new FileInputStream(new File("test.wav"));

        recognizer.startRecognition(stream);
	SpeechResult result;
        while ((result = recognizer.getResult()) != null) {
	    words.add(result.getHypothesis());
	}
    for(int i = 0; i < words.size(); i++) {
    	System.out.println(words.get(i));
    }
	recognizer.stopRecognition();
    }
}