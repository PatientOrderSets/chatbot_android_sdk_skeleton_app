package com.thinkresearch.skeltonapp

import android.app.Activity
import android.content.Intent
import android.os.Bundle
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


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.fab.setOnClickListener { view ->
            var bot = ChatBotSDK();
            bot.initialize(
                appId!!,
                baseUrl!!,
                origin!!,
                selectedLanguage!!,
                this
            )
            bot.start(this);
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
                origin = data?.getStringExtra("origin")
                baseUrl = data?.getStringExtra("baseUrl")
                selectedProjectType = data?.getStringExtra("selectedProjectType")
                selectedLanguage = data?.getStringExtra("selectedLanguage")

            }
        }


    override fun onSupportNavigateUp(): Boolean {
        val navController = findNavController(R.id.nav_host_fragment_content_main)
        return navController.navigateUp(appBarConfiguration) || super.onSupportNavigateUp()
    }

    var appId: String? = "yB9BJmrcH3bM4CShtMKB5qrw";
    var origin: String? = "test.ca.digital-front-door.stg.gcp.trchq.com"
    var baseUrl: String? = "test.ca.digital-front-door.stg.gcp.trchq.com"
    var selectedProjectType: String? = "";
    var selectedLanguage: String? = "fr";


    companion object {
        private const val REQUEST_CODE_SETTINGS = 1001
    }
}