package com.thinkresearch.skeltonapp

import android.app.Activity
import android.content.Intent
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AppCompatActivity
import androidx.navigation.findNavController
import androidx.navigation.ui.AppBarConfiguration
import androidx.navigation.ui.navigateUp
import com.thinkresearch.chatbot.ChatBotSDK
import com.thinkresearch.skeltonapp.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var appBarConfiguration: AppBarConfiguration
    private lateinit var binding: ActivityMainBinding

    var isProcessing = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.fab.setOnClickListener { view ->

            if (!isProcessing) {
                // Set the flag to true to indicate processing has started
                isProcessing = true

                // Initialize the ChatBotSDK
                val bot = ChatBotSDK()
                bot.initialize(
                    appId!!,
                    baseUrl!!,
                    selectedLanguage!!,
                    this
                )
                bot.start(this)

                // Listen for completion of the initialization and starting process
                // If successful or failed, reset the flag to allow further clicks
                // Adjust the delay time as needed depending on the initialization and starting process
                Handler(Looper.getMainLooper()).postDelayed({
                    isProcessing = false
                }, 2000) // Delay of 2 seconds
            }
        }


        binding.settingsButton.setOnClickListener {

            val intent = Intent(this, SettingActivity::class.java)
            resultLauncher.launch(intent)


        }
    }

    var resultLauncher =
        registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
            if (result.resultCode == Activity.RESULT_OK) {
                val data: Intent? = result.data


                appId = data?.getStringExtra("appId")
                baseUrl = data?.getStringExtra("baseUrl")
                selectedProjectType = data?.getStringExtra("selectedProjectType")
                selectedLanguage = data?.getStringExtra("selectedLanguage")

            }
        }


    override fun onSupportNavigateUp(): Boolean {
        val navController = findNavController(R.id.nav_host_fragment_content_main)
        return navController.navigateUp(appBarConfiguration) || super.onSupportNavigateUp()
    }

    private var appId: String? = "yB9BJmrcH3bM4CShtMKB5qrw";
    private var baseUrl: String? = "test.ca.digital-front-door.stg.gcp.trchq.com"
    private var selectedProjectType: String? = "";
    private var selectedLanguage: String? = "en";


    companion object {
        private const val REQUEST_CODE_SETTINGS = 1001
    }
}