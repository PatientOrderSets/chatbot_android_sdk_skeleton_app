# Chatbot Android SDK Integration Guide

Learn how to quickly integrate and start using the Chatbot Android SDK.

## Overview

This guide demonstrates how to install the Chatbot SDK, connect to the chatbot messenger, and run the sample Android application.

## Install SDK

To use the Chatbot Android SDK, you have two options: automatic installation using Gradle in Android Studio or manual installation by including the Android library (AAR file) in your Android Studio project.

**Minimum SDK**: 24  
**Supported architectures**: arm64-v8a, armeabi-v7a, x86_64

### Option A: Install using Android Studio and Gradle (Recommended)

1. Add the following configuration to your app `build.gradle` file:

```groovy
dependencies {
    implementation 'com.thinkresearch.chatbot:1.1.2’
}
```

2. Once you have updated your `build.gradle` file, sync your project by clicking on the "Sync Project With Gradle Files" button.

### Option B: Manual Install

For a manual install, follow these steps:

1. Download the latest SDK's AAR file from the [Releases section](#).
2. Copy the AAR file to your project's `app/libs` directory.
3. Add the following line in your module's `build.gradle`:

```groovy
dependencies {
    implementation(files("libs/app-release.aar"))
}
```

4. Once you have updated your `build.gradle` file, sync your project by clicking on the "Sync Project With Gradle Files" button.

## Initialize the Chatbot SDK in the Skeleton App

```java
ChatBotSDK bot = new ChatBotSDK();
bot.initialize("yB9BJmrcH3bM4CShtMKB5qrw",
               "test.ca.digital-front-door.stg.gcp.trchq.com",
               "test.ca.digital-front-door.stg.gcp.trchq.com",
               "en", this);
bot.start(this);
```

The `initialize` method takes 5 parameters:
1. `appID`
2. `baseUrl`
3. `originUrl`
4. `languageCode`
5. `Context`

Replace the parameters with your specific values accordingly.

Now you're ready to integrate and use the Chatbot Android SDK in your application. Happy coding!