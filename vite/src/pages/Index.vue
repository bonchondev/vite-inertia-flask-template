<script setup lang="ts">
import { ref } from "vue";
const frameworkName = ref("Vue");
defineProps<{
    amount: string;
}>();
</script>

<template>
    <div class="p-5">
        <img
            class="w-20"
            src="https://flask.palletsprojects.com/en/2.0.x/_static/flask-icon.png"
            alt="Flask logo"
        />
        <img
            class="w-20"
            src="https://avatars.githubusercontent.com/u/47703742?s=200&v=4"
            alt="Inertia logo"
        />
        <img
            class="w-20"
            src="https://vuejs.org/images/logo.png"
            alt="Vue logo"
        />

        <h1 class="title text-red-600 font-semibold text-2xl">
            Welcome to your Inertia {{ frameworkName }} app.
        </h1>

        <p class="info">
            For more information please visit the {{ amount }}
            <a href="https://flask-inertia.readthedocs.io/">documentation</a>
        </p>
    </div>
</template>
