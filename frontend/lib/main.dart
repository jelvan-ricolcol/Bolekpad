import 'package:flutter/material.dart';
import 'router/app_router.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'theme/bolek_colors.dart';

void main() {
  runApp(const ProviderScope(child: BolekpadApp()));
}

class BolekpadApp extends ConsumerWidget {
  const BolekpadApp({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final goRouter = ref.watch(goRouterProvider);

    return MaterialApp.router(
      title: 'Bolek Docs',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: BolekColors.primary),
        useMaterial3: true,
      ),
      routerConfig: goRouter,
    );
  }
}
