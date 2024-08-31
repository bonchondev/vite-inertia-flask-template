<script setup lang="ts">
import { ref } from "vue";
import { useQuery } from "@tanstack/vue-query";
import ky from "ky";
import { z } from "zod";
const frameworkName = ref("Vue");
defineProps<{
    amount: string;
}>();

const dataType = z.object({ dollars: z.number() });

type Data = z.infer<typeof dataType>;

const { data, isSuccess } = useQuery({
    queryKey: ["data"],
    queryFn: () => ky.post<Data>("/data").json(),
});
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
        <p v-if="isSuccess" class="text-3xl text-pink-400">
            {{ data?.dollars }}
        </p>
    </div>
</template>
