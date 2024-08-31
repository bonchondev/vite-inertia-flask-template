<script setup lang="ts">
import { ref } from "vue";
const frameworkName = ref("Vue");
defineProps<{
    amount: string;
}>();
</script>

<template>
    <div class="p-5 flex flex-col">
        <h1 class="title text-red-600 font-semibold text-2xl">
            Welcome to your Inertia {{ frameworkName }} app.
        </h1>

        <p class="info">
            For more information please visit the {{ amount }}
            <a href="https://flask-inertia.readthedocs.io/">documentation</a>
        </p>
    </div>
</template>
