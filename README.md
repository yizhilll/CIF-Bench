# CIF-Bench
This is the official repo for the paper [CIF-Bench: A Chinese Instruction-Following Benchmark for Evaluating the Generalizability of Large Language Models](https://arxiv.org/abs/2402.13109). 
The [project page](https://yizhilll.github.io/CIF-Bench/) has a more user-friendly UI for reading.

## Results


### Private Split

In the private split, there 5 instructions used for each task, hence derive $5 \times 150 \times 50=37500$ data instances for each model in evaluation.

| Model Name | Overall | Chinese Culture | Classification | Code | Commonsense | Creative NLG | Evaluation | Grammar | Linguistic | Motion Detection | NER | NLI | QA | Reasoning | Role Playing | Sentiment | Structured Data | Style Transfer | Summarization | Toxic | Translation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Baichuan2-13B-Chat | .529 | .520 | .674 | .333 | .641 | .497 | .686 | .542 | .528 | .578 | .563 | .632 | .569 | .515 | .752 | .624 | .459 | .462 | .332 | .441 | .273 |
| Qwen-72B-Chat | .519 | .486 | .630 | .296 | .634 | .508 | .634 | .458 | .520 | .494 | .550 | .626 | .565 | .528 | .762 | .613 | .496 | .459 | .282 | .608 | .271 |
| Yi-34B-Chat | .512 | .483 | .606 | .347 | .623 | .497 | .598 | .480 | .490 | .575 | .525 | .619 | .554 | .494 | .757 | .580 | .472 | .439 | .346 | .514 | .259 |
| Qwen-14B-Chat | .500 | .481 | .582 | .307 | .614 | .494 | .645 | .428 | .475 | .496 | .513 | .616 | .548 | .507 | .764 | .583 | .469 | .453 | .283 | .575 | .262 |
| Deepseek-Llm-67B-Chat | .471 | .467 | .571 | .259 | .577 | .486 | .549 | .442 | .476 | .475 | .509 | .566 | .496 | .439 | .711 | .546 | .409 | .436 | .262 | .570 | .235 |
| Baichuan-13B-Chat | .450 | .408 | .491 | .286 | .552 | .439 | .670 | .417 | .422 | .482 | .486 | .565 | .505 | .377 | .704 | .552 | .387 | .402 | .350 | .431 | .304 |
| Chatglm3-6B | .436 | .381 | .439 | .330 | .541 | .452 | .577 | .310 | .358 | .436 | .453 | .544 | .503 | .414 | .762 | .560 | .446 | .402 | .321 | .391 | .270 |
| Yi-6B-Chat | .417 | .402 | .454 | .313 | .523 | .425 | .506 | .383 | .383 | .487 | .396 | .523 | .457 | .369 | .754 | .482 | .401 | .380 | .310 | .455 | .227 |
| Baichuan2-7B-Chat | .412 | .437 | .647 | .160 | .520 | .402 | .580 | .511 | .444 | .455 | .407 | .489 | .395 | .406 | .670 | .517 | .342 | .298 | .101 | .463 | .138 |
| Chatglm2-6B | .352 | .278 | .469 | .346 | .403 | .424 | .535 | .274 | .397 | .406 | .240 | .397 | .352 | .326 | .714 | .438 | .298 | .313 | .320 | .461 | .190 |
| Chatglm-6B-Sft | .349 | .265 | .454 | .365 | .385 | .462 | .554 | .296 | .379 | .427 | .232 | .380 | .321 | .292 | .718 | .415 | .296 | .333 | .351 | .441 | .190 |
| Chinese-Llama2-Linly-13B | .344 | .250 | .462 | .311 | .399 | .429 | .557 | .273 | .358 | .385 | .268 | .390 | .330 | .313 | .653 | .433 | .279 | .332 | .292 | .457 | .181 |
| Gpt-3.5-Turbo-Sft | .343 | .269 | .427 | .298 | .389 | .395 | .575 | .325 | .365 | .389 | .226 | .382 | .394 | .345 | .710 | .433 | .324 | .266 | .290 | .397 | .225 |
| Chinese-Alpaca-2-13B | .341 | .242 | .421 | .356 | .382 | .442 | .602 | .256 | .363 | .430 | .210 | .376 | .334 | .317 | .714 | .459 | .299 | .316 | .308 | .452 | .200 |
| Chinese-Alpaca-13B | .334 | .250 | .399 | .348 | .364 | .435 | .616 | .275 | .349 | .421 | .223 | .370 | .309 | .319 | .724 | .426 | .285 | .307 | .298 | .445 | .181 |
| Chinese-Alpaca-7B | .334 | .216 | .412 | .378 | .381 | .425 | .576 | .265 | .359 | .393 | .243 | .383 | .326 | .295 | .710 | .409 | .301 | .327 | .325 | .405 | .186 |
| Chinese-Llama2-Linly-7B | .333 | .218 | .451 | .330 | .396 | .427 | .583 | .248 | .350 | .410 | .231 | .367 | .345 | .276 | .698 | .433 | .259 | .315 | .310 | .469 | .168 |
| Tigerbot-13B-Chat | .331 | .205 | .397 | .309 | .385 | .420 | .614 | .310 | .379 | .341 | .276 | .363 | .329 | .301 | .694 | .419 | .280 | .310 | .283 | .393 | .186 |
| Telechat-7B | .329 | .267 | .338 | .321 | .420 | .404 | .420 | .272 | .265 | .327 | .320 | .388 | .355 | .244 | .672 | .344 | .334 | .335 | .299 | .364 | .184 |
| Ziya-Llama-13B | .329 | .196 | .402 | .324 | .341 | .428 | .616 | .312 | .349 | .400 | .228 | .351 | .279 | .313 | .721 | .468 | .311 | .291 | .278 | .431 | .175 |
| Chinese-Alpaca-33B | .326 | .234 | .370 | .372 | .364 | .429 | .614 | .246 | .318 | .377 | .221 | .368 | .300 | .314 | .713 | .428 | .288 | .303 | .295 | .401 | .199 |
| Tigerbot-7B-Chat | .325 | .218 | .395 | .306 | .370 | .413 | .631 | .294 | .370 | .368 | .215 | .355 | .313 | .292 | .713 | .415 | .283 | .315 | .290 | .389 | .171 |
| Chinese-Alpaca-2-7B | .323 | .215 | .374 | .335 | .366 | .415 | .546 | .257 | .326 | .395 | .215 | .375 | .318 | .289 | .698 | .417 | .285 | .303 | .312 | .439 | .193 |
| Aquilachat-7B | .309 | .162 | .234 | .291 | .320 | .437 | .344 | .135 | .266 | .309 | .287 | .337 | .342 | .236 | .609 | .255 | .249 | .400 | .527 | .430 | .306 |
| Moss-Moon-003-Sft | .302 | .214 | .405 | .274 | .347 | .380 | .448 | .305 | .341 | .378 | .232 | .317 | .321 | .267 | .694 | .375 | .251 | .259 | .288 | .424 | .152 |
| Qwen-7B-Chat | .301 | .211 | .410 | .289 | .349 | .391 | .531 | .219 | .387 | .404 | .208 | .325 | .297 | .278 | .681 | .419 | .266 | .251 | .248 | .371 | .157 |
| Belle-13B-Sft | .264 | .198 | .307 | .285 | .316 | .349 | .409 | .237 | .305 | .222 | .177 | .317 | .284 | .242 | .631 | .299 | .244 | .222 | .234 | .296 | .133 |
| Cpm-Bee-10B | .244 | .234 | .377 | .024 | .278 | .311 | .255 | .302 | .278 | .327 | .148 | .286 | .224 | .147 | .603 | .277 | .117 | .263 | .220 | .352 | .125 |


### Public Split

In the public split, there is only one instruction used for each task, hence derive $1 \times 150 \times 50=7500$ data instances for each model in evaluation.

| Model Name | Overall | Chinese Culture | Classification | Code | Commonsense | Creative NLG | Evaluation | Grammar | Linguistic | Motion Detection | NER | NLI | QA | Reasoning | Role Playing | Sentiment | Structured Data | Style Transfer | Summarization | Toxic | Translation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Qwen-72B-Chat | .589 | .512 | .716 | .444 | .706 | .587 | .661 | .424 | .521 | .694 | .515 | .695 | .668 | .539 | .752 | .637 | .505 | .587 | .609 | .671 | .466 |
| Qwen-14B-Chat | .564 | .481 | .678 | .416 | .657 | .567 | .669 | .396 | .485 | .663 | .486 | .647 | .609 | .498 | .757 | .638 | .460 | .610 | .629 | .691 | .467 |
| Deepseek-LLM-67B-Chat | .526 | .477 | .617 | .364 | .609 | .559 | .573 | .374 | .458 | .631 | .493 | .588 | .624 | .444 | .694 | .592 | .384 | .576 | .594 | .666 | .439 |
| gpt-3.5-Public-SFT | .522 | .316 | .611 | .492 | .578 | .538 | .639 | .377 | .447 | .580 | .492 | .587 | .565 | .498 | .745 | .583 | .444 | .501 | .620 | .643 | .452 |
| Yi-34B-Chat | .516 | .452 | .607 | .437 | .624 | .516 | .545 | .254 | .382 | .671 | .398 | .631 | .592 | .460 | .761 | .566 | .440 | .551 | .610 | .608 | .408 |
| Baichuan2-13B-Chat | .512 | .446 | .623 | .403 | .600 | .505 | .582 | .352 | .423 | .633 | .435 | .600 | .591 | .474 | .751 | .597 | .434 | .525 | .572 | .494 | .372 |
| Tigerbot-13B-Chat | .494 | .350 | .558 | .447 | .599 | .528 | .707 | .352 | .447 | .551 | .498 | .571 | .569 | .413 | .732 | .560 | .365 | .502 | .607 | .601 | .306 |
| Chinese-Alpaca-2-13B | .492 | .260 | .572 | .434 | .533 | .562 | .574 | .318 | .417 | .624 | .467 | .566 | .545 | .420 | .712 | .595 | .382 | .488 | .641 | .740 | .347 |
| Chinese-Alpaca-33B | .484 | .274 | .546 | .470 | .527 | .540 | .703 | .332 | .382 | .582 | .464 | .550 | .506 | .423 | .732 | .548 | .342 | .494 | .629 | .648 | .334 |
| Ziya-Llama-13B | .479 | .287 | .550 | .422 | .523 | .551 | .650 | .294 | .384 | .610 | .437 | .546 | .499 | .404 | .749 | .582 | .367 | .499 | .629 | .722 | .313 |
| Chinese-Llama2-Linly-13B | .479 | .286 | .623 | .439 | .549 | .535 | .626 | .286 | .403 | .587 | .468 | .563 | .524 | .411 | .676 | .561 | .359 | .482 | .602 | .696 | .313 |
| Tigerbot-7B-Chat | .478 | .354 | .528 | .440 | .570 | .540 | .708 | .314 | .430 | .528 | .413 | .532 | .554 | .393 | .731 | .583 | .351 | .519 | .630 | .614 | .291 |
| ChatGLM3-6B | .472 | .321 | .488 | .436 | .527 | .503 | .588 | .290 | .328 | .574 | .415 | .557 | .526 | .397 | .749 | .612 | .431 | .529 | .620 | .589 | .392 |
| Chinese-Alpaca-13B | .471 | .264 | .553 | .443 | .495 | .525 | .587 | .334 | .394 | .653 | .457 | .524 | .513 | .402 | .726 | .526 | .323 | .486 | .628 | .702 | .336 |
| ChatGLM2-6B | .464 | .334 | .532 | .436 | .522 | .527 | .651 | .314 | .395 | .536 | .402 | .520 | .533 | .407 | .725 | .506 | .363 | .480 | .627 | .661 | .303 |
| Chinese-Alpaca-7B | .452 | .237 | .536 | .438 | .484 | .502 | .672 | .318 | .389 | .652 | .394 | .504 | .501 | .351 | .699 | .543 | .365 | .478 | .623 | .711 | .328 |
| Chinese-Alpaca-2-7B | .448 | .251 | .472 | .435 | .480 | .532 | .577 | .268 | .348 | .596 | .431 | .509 | .493 | .344 | .703 | .510 | .334 | .483 | .637 | .596 | .343 |
| Chinese-Llama2-Linly-7B | .443 | .264 | .558 | .419 | .497 | .522 | .664 | .236 | .381 | .593 | .381 | .496 | .546 | .350 | .713 | .559 | .323 | .495 | .603 | .584 | .293 |
| Qwen-7B-Chat | .442 | .313 | .549 | .404 | .520 | .515 | .646 | .244 | .411 | .570 | .368 | .489 | .514 | .384 | .713 | .563 | .328 | .463 | .576 | .639 | .281 |
| ChatGLM-6B | .440 | .311 | .499 | .446 | .484 | .548 | .558 | .278 | .382 | .484 | .386 | .480 | .483 | .353 | .738 | .460 | .346 | .480 | .633 | .543 | .322 |
| Baichuan-13B-Chat | .426 | .355 | .416 | .361 | .516 | .416 | .564 | .324 | .374 | .380 | .394 | .531 | .584 | .339 | .668 | .478 | .402 | .459 | .559 | .497 | .392 |
| Yi-6B-Chat | .420 | .320 | .439 | .395 | .489 | .449 | .493 | .230 | .293 | .587 | .341 | .496 | .516 | .344 | .742 | .488 | .348 | .498 | .627 | .510 | .285 |
| CPM-Bee-10B | .415 | .382 | .455 | .284 | .431 | .508 | .300 | .317 | .367 | .494 | .397 | .451 | .472 | .304 | .647 | .329 | .284 | .538 | .534 | .486 | .305 |
| Moss-Moon-003-SFT | .399 | .233 | .465 | .389 | .427 | .482 | .509 | .274 | .369 | .526 | .385 | .403 | .457 | .325 | .712 | .450 | .304 | .435 | .594 | .542 | .308 |
| Belle-SFT-Public | .397 | .196 | .503 | .376 | .426 | .472 | .543 | .269 | .371 | .512 | .356 | .450 | .430 | .338 | .645 | .426 | .300 | .398 | .558 | .683 | .224 |
| Telechat-7B | .350 | .172 | .299 | .438 | .386 | .456 | .400 | .138 | .202 | .412 | .322 | .375 | .414 | .261 | .660 | .341 | .320 | .462 | .639 | .494 | .304 |
| Aquilachat-7B | .350 | .203 | .270 | .357 | .404 | .449 | .394 | .090 | .260 | .348 | .322 | .385 | .426 | .274 | .595 | .308 | .267 | .434 | .607 | .409 | .355 |
| Baichuan2-7B-Chat | .339 | .345 | .595 | .154 | .455 | .327 | .523 | .362 | .354 | .466 | .233 | .414 | .349 | .339 | .673 | .429 | .300 | .246 | .097 | .357 | .130 |


## TODOs

- [ ] Inference code for demo model.
- [ ] Evaluation code and prompts.
- [ ] Public split data.

## Reference

```
@article{li2024cifbench,
      title={CIF-Bench: A Chinese Instruction-Following Benchmark for Evaluating the Generalizability of Large Language Models}, 
      author={Yizhi LI and Ge Zhang and Xingwei Qu and Jiali Li and Zhaoqun Li and Zekun Wang and Hao Li and Ruibin Yuan and Yinghao Ma and Kai Zhang and Wangchunshu Zhou and Yiming Liang and Lei Zhang and Lei Ma and Jiajun Zhang and Zuowen Li and Stephen W. Huang and Chenghua Lin and Wenhu Chen and Jie Fu},
      year={2024},
      eprint={2402.13109},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```